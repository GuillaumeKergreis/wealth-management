import datetime

from rest_framework import viewsets

from market_data.data_sources.boursorama_market import BoursoramaMarket
from market_data.serializers import *


class DataSourceViewSet(viewsets.ModelViewSet):
    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer


class MarketAssetTypeViewSet(viewsets.ModelViewSet):
    queryset = MarketAssetType.objects.all()
    serializer_class = MarketAssetTypeSerializer


class MarketplaceViewSet(viewsets.ModelViewSet):
    queryset = Marketplace.objects.all()
    serializer_class = MarketplaceSerializer


class BusinessSectorViewSet(viewsets.ModelViewSet):
    queryset = BusinessSector.objects.all()
    serializer_class = BusinessSectorSerializer


class IndexViewSet(viewsets.ModelViewSet):
    queryset = Index.objects.all()
    serializer_class = IndexSerializer


class MarketAssetViewSet(viewsets.ModelViewSet):
    queryset = MarketAsset.objects.all()
    serializer_class = MarketAssetSerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class ExchangeRateViewSet(viewsets.ModelViewSet):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer


class MarketAssetValueViewSet(viewsets.ModelViewSet):
    queryset = MarketAssetValue.objects.all()
    serializer_class = MarketAssetValueSerializer


def synchronize_data_source(data_source_name: str):
    if data_source_name == 'Boursorama':
        synchronize_boursorama_market_data()


def synchronize_boursorama_market_data():
    boursorama_data_source, _ = DataSource.objects.get_or_create(name='Boursorama')
    print(boursorama_data_source)

    for market_asset in boursorama_data_source.market_assets.all():
        print(market_asset)
        if market_asset.link:
            boursorama_market_asset = BoursoramaMarket.get_market_asset_by_link(market_asset.link)
        else:
            boursorama_market_asset = BoursoramaMarket.get_market_asset_by_reference(market_asset.reference)

        market_asset.link = boursorama_market_asset.link
        market_asset.value = boursorama_market_asset.value
        market_asset.save()

        boursorama_market_asset_values = BoursoramaMarket.get_market_asset_values(market_asset.reference)
        for asset_value in boursorama_market_asset_values:
            market_asset_value, _ = MarketAssetValue.objects.get_or_create(
                market_asset=market_asset,
                date=asset_value.date,
                defaults={
                    'open': asset_value.open,
                    'high': asset_value.high,
                    'low': asset_value.low,
                    'close': asset_value.close,
                    'volume': asset_value.volume,
                }
            )
            print(market_asset_value)

    # Missing currencies creation
    euro_currency = Currency.objects.get(code='EUR')
    for _, currency_line in BoursoramaMarket.get_currency_exchange_rates(euro_currency.code).iterrows():
        country = currency_line['Libellé']
        name = currency_line['Monnaie'].split(' - ')[0]
        code = currency_line['Monnaie'].split(' - ')[1]

        currency, _ = Currency.objects.get_or_create(code=code, defaults={
            'country': country,
            'name': name
        })

        print(currency)

    boursorama_currencies_marketplace, _ = Marketplace.objects.get_or_create(
        name='Swiss Stock Exchange',
        symbol='SIX',
    )

    # We delete all the today exchange rate (so that we can bulk insert then)
    ExchangeRate.objects.filter(
        data_source=boursorama_data_source,
        marketplace=boursorama_currencies_marketplace,
        date=datetime.date.today()
    ).delete()

    # Exchange rates enrichment
    for from_currency in Currency.objects.all():
        to_currency_exchange_rates = BoursoramaMarket.get_currency_exchange_rates(from_currency.code)
        exchange_rates_to_insert = []
        for _, to_currency_line in to_currency_exchange_rates.iterrows():
            code = to_currency_line['Monnaie'].split(' - ')[1]
            rate = float(str(to_currency_line['Dernier']).replace(' ', ''))
            to_currency = Currency.objects.get(code=code)

            print(f'{from_currency.code} --> {to_currency.code} : {rate}')

            exchange_rates_to_insert.append(
                ExchangeRate(
                data_source=boursorama_data_source,
                marketplace=boursorama_currencies_marketplace,
                date=datetime.date.today(),
                from_currency=from_currency,
                to_currency=to_currency,
                rate=rate
            ))

        ExchangeRate.objects.bulk_create(exchange_rates_to_insert)






