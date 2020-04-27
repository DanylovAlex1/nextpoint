from django.db import models

# Create your models here.

class Usd(models.Model):
    date = models.DateField(db_index=True,verbose_name='Date', null=False)
    buy=models.FloatField(verbose_name='Buying rate', null=False)
    sale = models.FloatField(verbose_name='Selling rate',null=False)




