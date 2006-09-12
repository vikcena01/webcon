from django.db import models
from webcon.common.models import Country, Address
from webcon.hotels.models import Hotel

# Create your models here.


class Contractor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(maxlength=255)
#    address = models.CharField(maxlength=255)
#    city = models.CharField(maxlength=50)
#    state = models.ForeignKey(State, db_column='state')
#    country = models.ForeignKey(Country)
    phone = models.CharField(maxlength=40)
    email = models.CharField(maxlength=40)
    account = models.CharField(maxlength=32)
    address = models.ForeignKey(Address)

    class Meta:
        db_table = 'contractor'


class Conference(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(maxlength=256)
    description = models.TextField()
    # country = models.ForeignKey(Country, db_column='country')
    # city = models.CharField(maxlength=64)
    contractor = models.ForeignKey(Contractor)
    start_date = models.DateField()
    end_date = models.DateField()
    nights = models.SmallIntegerField()
    price = models.FloatField(max_digits=65535, decimal_places=65531)
    cost = models.FloatField(max_digits=65535, decimal_places=65531)
    active = models.BooleanField()
    address = models.ForeignKey(Address)
    
    class Meta:
        db_table = 'conference'



class ConferenceHotel(models.Model):
    id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel)
    conference = models.ForeignKey(Conference)
    class Meta:
        db_table = 'conference_hotel'



class Roomclass(models.Model):
    id = models.AutoField(primary_key=True)
    conference_hotel = models.ForeignKey(ConferenceHotel)
    size = models.SmallIntegerField()
    price = models.FloatField(max_digits=65535, decimal_places=65531)
    cost = models.FloatField(max_digits=65535, decimal_places=65531)
    class Meta:
        db_table = 'roomclass'



class Room(models.Model):
    id = models.AutoField(primary_key=True)
    roomclass = models.ForeignKey(Roomclass)
    number = models.CharField(maxlength=16)
    class Meta:
        db_table = 'room'



class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(maxlength=40)
    description = models.TextField()
    place = models.CharField(maxlength=256)
    time = models.DateTimeField()
    class Meta:
        db_table = 'event'


class Extra(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(maxlength=40)
    description = models.TextField()
    place = models.CharField(maxlength=256)
    time = models.DateTimeField()
    price = models.FloatField(max_digits=65535, decimal_places=65531)
    cost = models.FloatField(max_digits=65535, decimal_places=65531)
    class Meta:
        db_table = 'extra'

