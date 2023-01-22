from rest_framework import serializers

from market_data.models import *


class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSource
        fields = '__all__'


class MarketAssetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketAssetType
        fields = '__all__'


class MarketplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketplace
        fields = '__all__'


class MarketAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketAsset
        fields = '__all__'


class BusinessSectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessSector
        fields = '__all__'


class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = '__all__'


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = '__all__'


class MarketAssetValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketAssetValue
        fields = '__all__'
