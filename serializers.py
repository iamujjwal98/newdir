from currency.models import CurrencyDetails, CurrencyHeader

from rest_framework import serializers

class CurrencyHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyHeader
        fields = ['currencyCode','currencyId','currencyName']
           
class CurrencyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyDetails
        fields =['exchangeRateType','daysToSpotSettlement','deactivationDate']  