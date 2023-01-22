from django.db import models


class DataSource(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class MarketAssetType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Marketplace(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class BusinessSector(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Index(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=255)  # Euro
    symbol = models.CharField(max_length=255, null=True, blank=True)  # €
    code = models.CharField(max_length=255)  # EUR
    country = models.CharField(max_length=255, null=True, blank=True)  # Europe

    def __str__(self):
        return f'{self.name} ({self.code})'


class ExchangeRate(models.Model):
    data_source = models.ForeignKey(to=DataSource, on_delete=models.CASCADE, related_name='exchange_rates')
    marketplace = models.ForeignKey(to=Marketplace, on_delete=models.SET_NULL, related_name='exchange_rates', null=True, blank=True)
    date = models.DateField()
    rate = models.FloatField()
    from_currency = models.ForeignKey(to=Currency, on_delete=models.CASCADE, related_name='from_currency_exchange_rates')
    to_currency = models.ForeignKey(to=Currency, on_delete=models.CASCADE, related_name='to_currency_exchange_rates')

    def __str__(self):
        return f'{self.from_currency.name}/{self.to_currency.name}'


class MarketAsset(models.Model):
    data_source = models.ForeignKey(to=DataSource, on_delete=models.CASCADE, related_name='market_assets')
    link = models.CharField(max_length=255, null=True, blank=True)
    reference = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    value = models.FloatField()
    currency = models.ForeignKey(to=Currency, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)
    marketplace = models.ForeignKey(to=Marketplace, on_delete=models.SET_NULL, related_name='market_assets', null=True, blank=True)
    isin_code = models.CharField(max_length=255, null=True, blank=True)
    ticker = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    type = models.ForeignKey(to=MarketAssetType, on_delete=models.SET_NULL, related_name='market_assets', null=True, blank=True)
    business_sector = models.ForeignKey(to=BusinessSector, on_delete=models.SET_NULL, related_name='market_assets', null=True, blank=True)
    index = models.ForeignKey(to=Index, on_delete=models.SET_NULL, related_name='market_assets', null=True, blank=True)

    def __str__(self):
        return self.name


class MarketAssetValue(models.Model):
    market_asset = models.ForeignKey(to=MarketAsset, on_delete=models.CASCADE, related_name='values')
    date = models.DateField()
    open = models.FloatField(null=True, blank=True)
    high = models.FloatField(null=True, blank=True)
    low = models.FloatField(null=True, blank=True)
    close = models.FloatField()
    volume = models.FloatField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.market_asset.name} : {self.date} - {self.close} {self.market_asset.currency.code}'
