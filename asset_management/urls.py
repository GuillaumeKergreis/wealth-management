from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('users', UsersViewSet)
router.register('institution-types', InstitutionTypeViewSet)
router.register('institutions', InstitutionViewSet)
router.register('user-institutions', UserInstitutionViewSet)
router.register('account-types', AccountTypeViewSet)
router.register('accounts', AccountViewSet)
router.register('transactions', TransactionViewSet)
router.register('account-values', AccountValueViewSet)
router.register('asset-types', AssetTypeViewSet)
router.register('asset-tags', AssetTagViewSet)
router.register('asset_management', AssetViewSet)
router.register('asset-values', AssetValueViewSet)
router.register('asset-quantities', AssetQuantityViewSet)

urlpatterns = [
    path('', include(router.urls), name='asset_management'),
]
