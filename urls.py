from django.urls import path, include
from currency.views import CurrencyDetailsList, CurrencyHeaderList

urlpatterns = [
    path('CurrencyHeader/', CurrencyHeaderList.as_view()),
    path('CurrencyDetails/', CurrencyDetailsList.as_view()),
    
]

