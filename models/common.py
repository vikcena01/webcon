from django.db import models

# Create your models here.

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(maxlength=60)
    class Meta:
        db_table = 'country'


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(maxlength=256)
    city = models.CharField(maxlength=64)
    country = models.ForeignKey(Country)
    zipcode = models.CharField(maxlength=16)

    class Meta:
        db_table = 'address'
