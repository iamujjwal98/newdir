# Create your views here.
from currency.models import CurrencyDetails, CurrencyHeader
from currency.serializers import CurrencyDetailsSerializer, CurrencyHeaderSerializer
from rest_framework import generics, permissions, serializers
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

#from django.contrib import admin

class CurrencyHeaderList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = CurrencyHeader.objects.all()
    serializer_class = CurrencyHeaderSerializer
    
    
class CurrencyDetailsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = CurrencyDetails.objects.all()
    serializer_class = CurrencyDetailsSerializer    


