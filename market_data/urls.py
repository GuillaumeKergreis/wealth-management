from django.urls import include, path
from rest_framework import routers

from market_data.views import *

router = routers.DefaultRouter()

router.register('data-source', DataSourceViewSet)
router.register('market-asset-type', MarketAssetTypeViewSet)
router.register('marketplace', MarketplaceViewSet)
router.register('market-asset', MarketAssetViewSet)
router.register('currency', CurrencyViewSet)
router.register('exchange-rate', ExchangeRateViewSet)
router.register('market-asset-value', MarketAssetValueViewSet)

urlpatterns = [
    path('', include(router.urls), name='market_data'),
]
