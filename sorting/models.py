from django.db import models

# Create your models here.
class Entries(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True,unique=True)
    currentRank = models.IntegerField(blank=True,null=True,default=0)
    previousRrank = models.IntegerField(blank=True,null=True,default=0)
    priceChange = models.FloatField(blank=True,null=True,default=0)
    price = models.FloatField(blank=True,null=True,default=0)

    def __str__(self):
        return self.name