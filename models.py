from django.db import models
from django.utils import timezone
# Create your models here.

class CurrencyHeader(models.Model):
    currencyCode=models.CharField(max_length=100)
    currencyId=models.IntegerField() 
    currencyName=models.TextField()
    
    def __str__(self):
        return self.currencyName  
    


class CurrencyDetails(models.Model):
    exchangeRateType=models.TextField()
    daysToSpotSettlement=models.IntegerField() 
    deactivationDate=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.exchangeRateType
    
