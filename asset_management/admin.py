from django.contrib import admin

from asset_management.models import *

admin.site.register(InstitutionType)
admin.site.register(Institution)
admin.site.register(UserInstitution)
admin.site.register(AccountType)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(AccountValue)
admin.site.register(AssetType)
admin.site.register(AssetTag)
admin.site.register(Asset)
admin.site.register(AssetValue)
admin.site.register(AssetQuantity)
