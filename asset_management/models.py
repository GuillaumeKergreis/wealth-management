from django.contrib.auth.models import User
from django.db import models

from market_data.models import Currency, MarketAsset


class InstitutionType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    type = models.ForeignKey(to=InstitutionType, on_delete=models.SET_NULL, related_name='institutions', null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    background = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class UserInstitution(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='user_institutions')
    institution = models.ForeignKey(to=Institution, on_delete=models.CASCADE, related_name='user_institutions')
    identifier = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.institution.name}'


class AccountType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Account(models.Model):
    user_institution = models.ForeignKey(to=UserInstitution, on_delete=models.CASCADE, related_name='accounts')
    reference = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    value = models.FloatField()
    unrealized_pnl_value = models.FloatField(null=True, blank=True)
    currency = models.ForeignKey(to=Currency, on_delete=models.CASCADE)
    type = models.ForeignKey(to=AccountType, on_delete=models.SET_NULL, related_name='accounts', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    account_number = models.CharField(max_length=255, null=True, blank=True)
    iban = models.CharField(max_length=255, null=True, blank=True)
    bic = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.user_institution.institution.name} - {self.name}'


class Transaction(models.Model):
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE, related_name='transactions')
    date = models.DateField()
    amount = models.FloatField()
    label = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class AccountValue(models.Model):
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE, related_name='values')
    date = models.DateField()
    value = models.FloatField()

    def __str__(self):
        return f'{self.account.name} - {self.date} : {self.value} {self.account.currency.code}'


class AssetType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AssetTag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Asset(models.Model):
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE, related_name='assets')
    name = models.CharField(max_length=255)
    value = models.FloatField()
    break_even_price = models.FloatField(null=True, blank=True)
    currency = models.ForeignKey(to=Currency, on_delete=models.CASCADE)
    quantity = models.FloatField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    type = models.ForeignKey(to=AssetType, on_delete=models.SET_NULL, related_name='assets', null=True, blank=True)
    tags = models.ManyToManyField(to=AssetTag, related_name='assets')
    market_asset = models.ForeignKey(to=MarketAsset, on_delete=models.SET_NULL, related_name='assets', null=True, blank=True)

    def __str__(self):
        return self.name


class AssetValue(models.Model):
    asset = models.ForeignKey(to=Asset, on_delete=models.CASCADE, related_name='asset_values')
    date = models.DateField()
    value = models.FloatField()
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.asset.name} - {self.value} {self.asset.currency.code}'


class AssetQuantity(models.Model):
    asset = models.ForeignKey(to=Asset, on_delete=models.CASCADE, related_name='asset_quantities')
    date = models.DateField()
    quantity = models.FloatField()
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.asset.name} - quantity : {self.quantity}'
