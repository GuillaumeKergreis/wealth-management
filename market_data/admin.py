from django.contrib import admin

from market_data.models import *

admin.site.register(DataSource)
admin.site.register(MarketAssetType)
admin.site.register(Marketplace)
admin.site.register(BusinessSector)
admin.site.register(Index)
admin.site.register(MarketAsset)
admin.site.register(Currency)
admin.site.register(ExchangeRate)
admin.site.register(MarketAssetValue)
