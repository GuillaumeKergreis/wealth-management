from rest_framework import viewsets

from asset_management.institutions.boursorama import Boursorama, BoursoramaAccountType
from asset_management.serializers import *
from asset_management.tasks import synchronize_boursorama


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class InstitutionTypeViewSet(viewsets.ModelViewSet):
    queryset = InstitutionType.objects.all()
    serializer_class = InstitutionTypeSerializer


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class UserInstitutionViewSet(viewsets.ModelViewSet):
    queryset = UserInstitution.objects.all()
    serializer_class = UserInstitutionSerializer


class AccountTypeViewSet(viewsets.ModelViewSet):
    queryset = AccountType.objects.all()
    serializer_class = AccountTypeSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class AccountValueViewSet(viewsets.ModelViewSet):
    queryset = AccountValue.objects.all()
    serializer_class = AccountValueSerializer


class AssetTypeViewSet(viewsets.ModelViewSet):
    queryset = AssetType.objects.all()
    serializer_class = AssetTypeSerializer


class AssetTagViewSet(viewsets.ModelViewSet):
    queryset = AssetTag.objects.all()
    serializer_class = AssetTagSerializer


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


class AssetValueViewSet(viewsets.ModelViewSet):
    queryset = AssetValue.objects.all()
    serializer_class = AssetValueSerializer


class AssetQuantityViewSet(viewsets.ModelViewSet):
    queryset = AssetQuantity.objects.all()
    serializer_class = AssetQuantitySerializer


def synchronize_institutions():
    synchronize_boursorama.delay()

