from django.db import models
from webcon.models.m_common import Address
from webcon.models.m_hotels import Hotel
from webcon.models.m_contrs import Contractor

# Create your models here.

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
    reg_deadline = models.DateTimeField()

    def get_absolute_url(self):
        return "/confs/%s" % self.id

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

