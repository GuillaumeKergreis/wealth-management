import datetime
from dataclasses import dataclass
from typing import Optional, List

import bs4
import pandas as pd
import requests
from pandas import DataFrame


@dataclass
class BoursoramaMarketAsset:
    link: str
    reference: str
    asset_name: str
    value: float
    currency_code: str
    daily_variation: float
    isin_code: str
    ticker: str
    marketplace_name: str
    business_sector_name: str
    index_name: str


@dataclass
class BoursoramaMarketAssetValue:
    date: datetime.date
    open: float
    high: float
    low: float
    close: float
    volume: float


def string_to_number(string: str) -> float:
    return float(string.strip().replace(' ', '').replace(' ', '').replace('€', '').replace('%', '').replace(',', '.'))


class BoursoramaMarket:

    @staticmethod
    def get_market_assets_by_name(name: str) -> DataFrame:
        """
                                   Libellé               Place      Cours Variation
        0                    TOTALENERGIES      Euronext Paris  59.73 EUR    +0.47%
        1       TOTALENERGIES TOT OPEN EUR      Euronext Paris   100.50 %     0.00%
        2                    TOTALENERGIES               XETRA  59.80 EUR    +0.34%
        3                    TOTALENERGIES  Euronext Bruxelles  59.73 EUR    +0.47%
        4  TOTALENERGIES TOTAL OPEN -S EUR      Euronext Paris    94.51 %     0.00%
        """
        df = pd.DataFrame()
        page = 1
        while not 'Aucune donnée à afficher' in requests.get(
                f'https://www.boursorama.com/recherche/_instruments/{name}?page={page}').text:
            df = pd.concat([df, pd.read_html(
                requests.get(f'https://www.boursorama.com/recherche/_instruments/{name}?page={page}').text)[0]],
                           ignore_index=True)
            page += 1
        return df

    @staticmethod
    def get_market_asset_by_link(link: str) -> Optional[BoursoramaMarketAsset]:
        res = requests.get(link)
        return BoursoramaMarket.extract_market_asset_from_res(res)

    @staticmethod
    def get_market_asset_by_reference(reference: str) -> Optional[BoursoramaMarketAsset]:
        res = requests.get(f'https://www.boursorama.com/cours/{reference}')
        return BoursoramaMarket.extract_market_asset_from_res(res)

    @staticmethod
    def get_market_asset_by_isin_code(isin_code: str) -> Optional[BoursoramaMarketAsset]:
        res = requests.get(f'https://www.boursorama.com/cours/{isin_code}')
        return BoursoramaMarket.extract_market_asset_from_res(res)

    @staticmethod
    def extract_market_asset_from_res(res) -> Optional[BoursoramaMarketAsset]:
        if 'Aucune donnée à afficher' in res.text:
            return None
        else:
            bs = bs4.BeautifulSoup(res.text, features='lxml')
            link = res.url
            reference = res.url.split('/')[-2].strip()

            try:
                asset_name = bs.select_one('.c-faceplate__company-link').getText().strip()
            except:
                asset_name = None

            try:
                value = float(bs.select_one('.c-instrument.c-instrument--last').getText().strip())
            except:
                value = None

            try:
                currency_code = bs.select_one('.c-faceplate__price-currency').getText().strip()
            except:
                currency_code = None

            try:
                daily_variation = string_to_number(bs.select_one('.c-instrument.c-instrument--variation').getText().strip())
            except:
                daily_variation = None

            try:
                isin_code = bs.select_one('.c-faceplate__isin').getText().split(' ')[0].strip()
            except:
                isin_code = None

            try:
                ticker = bs.select_one('.c-faceplate__isin').getText().split(' ')[1].strip()
            except:
                ticker = None

            try:
                marketplace_name = bs.select_one('.c-faceplate__real-time').getText().strip()
            except:
                marketplace_name = None

            try:
                business_sector_name = bs.select_one('#main-content > div > section.l-quotepage > header > div > div > div.c-faceplate__chart > div.c-faceplate__chart-bottom > div > ul > li:nth-child(1) > p.c-list-info__value.u-color-big-stone > a').getText().strip()
            except:
                business_sector_name = None

            try:
                index_name = bs.select_one('#main-content > div > section.l-quotepage > header > div > div > div.c-faceplate__chart > div.c-faceplate__chart-bottom > div > ul > li:nth-child(2) > p.c-list-info__value.u-color-big-stone > a').getText().strip()
            except:
                index_name = None


            return BoursoramaMarketAsset(
                link=link,
                reference=reference,
                asset_name=asset_name,
                value=value,
                currency_code=currency_code,
                daily_variation=daily_variation,
                isin_code=isin_code,
                ticker=ticker,
                marketplace_name=marketplace_name,
                business_sector_name=business_sector_name,
                index_name=index_name
            )

    @staticmethod
    def get_market_asset_values(asset_reference: str) -> List[BoursoramaMarketAssetValue]:
        res = requests.get(
            f'https://www.boursorama.com/bourse/action/graph/ws/GetTicksEOD?guid=&length=3650&period=356&symbol={asset_reference}')
        """
        {"d":
            {
                "Name":"DANONE",
                "SymbolId":"1rPBN",
                "Xperiod":"356",
                "QuoteTab":[
                    {"d":15719,"o":48.38106,"h":48.38593,"l":47.933,"c":47.94274,"v":1157468}
                ]
            }
        }
        """
        quotes = res.json()['d']['QuoteTab']

        asset_market_values: List[BoursoramaMarketAssetValue] = []
        for quote in quotes:
            date = datetime.date(1970, 1, 1) + datetime.timedelta(days=quote['d'])
            asset_market_values.append(
                BoursoramaMarketAssetValue(
                    date=date,
                    open=quote['o'],
                    high=quote['h'],
                    low=quote['l'],
                    close=quote['c'],
                    volume=quote['v'],
                )
            )

        return asset_market_values

    @staticmethod
    def get_currency_exchange_rates(currency_code: str) -> DataFrame:
        """
                  Libellé               Monnaie   Dernier     Var
        0     Afghanistan         Afghani - AFN   97.5185  -0.01%
        1  Afrique du Sud            Rand - ZAR   18.2809   0.00%
        2         Albanie             Lek - ALL  115.6429  -0.60%
        3         Algérie  Dinar Algérien - DZD  147.4850  -0.25%
        4          Angola          Kwanza - AOA  549.7498   0.00%
        """
        res = requests.get(f'https://www.boursorama.com/bourse/devises/parite/_detail-parite/{currency_code}')
        return pd.read_html(res.text)[0]

