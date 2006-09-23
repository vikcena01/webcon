from django.db import models
from webcon.models.common import Address
from webcon.models.hotels import Hotel
from webcon.models.contrs import Contractor

# Create your models here.

class Conference(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(maxlength=256)
    description = models.TextField()
    contractor = models.ForeignKey(Contractor)
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.FloatField(max_digits=65535, decimal_places=65531)
    active = models.BooleanField()
    reg_deadline = models.DateTimeField()
    hotel = models.ForeignKey(Hotel)
    
    class Meta:
        db_table = 'conference'



class ArchiveConference(models.Model):  
    id = models.AutoField(primary_key=True)
    name = models.CharField(maxlength=256)
    description = models.TextField()
    contractor = models.ForeignKey(Contractor)
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.FloatField(max_digits=65535, decimal_places=65531)
    active = models.BooleanField()
    reg_deadline = models.DateTimeField()
    hotel = models.ForeignKey(Hotel)
       
    class Meta:
        db_table = 'archive_conferences'



class ActualConference(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(maxlength=256)
    description = models.TextField()
    contractor = models.ForeignKey(Contractor)
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.FloatField(max_digits=65535, decimal_places=65531)
    active = models.BooleanField()
    reg_deadline = models.DateTimeField()
    hotel = models.ForeignKey(Hotel)
    
    class Meta:
        db_table = 'actual_conferences'



class CommingConference(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(maxlength=256)
    description = models.TextField()
    contractor = models.ForeignKey(Contractor)
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.FloatField(max_digits=65535, decimal_places=65531)
    active = models.BooleanField()
    reg_deadline = models.DateTimeField()
    hotel = models.ForeignKey(Hotel)
    
    class Meta:
        db_table = 'comming_conferences'






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
    cost = models.FloatField(max_digits=65535, decimal_places=65531)
    class Meta:
        db_table = 'extra'

