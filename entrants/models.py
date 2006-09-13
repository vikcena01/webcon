from django.db import models
from webcon.common.models import Country
from webcon.confs.models import Room, Extra

# Create your models here.

class Entrant(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(maxlength=40)
    lastname = models.CharField(maxlength=40)
    country = models.ForeignKey(Country, db_column='country')
    city = models.CharField(maxlength=64)
    zipcode = models.CharField(maxlength=16)
    address = models.CharField(maxlength=256)
    email = models.CharField(maxlength=40)
    phone = models.CharField(maxlength=16)
    birthdate = models.DateField()
    sex = models.CharField(maxlength=1)
    passwd_hash = models.CharField(maxlength=32)
    # conf_price = models.FloatField(max_digits=65535, decimal_places=65531)
    registered = models.DateTimeField()
    # arrived = models.DateTimeField()
    # payment_type = models.SmallIntegerField()
    # caution = models.TextField()
    # rating = models.SmallIntegerField()
    # comment = models.TextField()
    # annotation = models.TextField()
    # room = models.ForeignKey(Room)
    # nights = models.SmallIntegerField()
    last_good_login = models.DateTimeField()
    last_bad_login = models.DateTimeField()

    def get_absolute_url(self):
        return "/entra/%s" % self.id

    class Meta:
        db_table = 'entrant'
    class Admin:
        pass


class EntrantExtra(models.Model):
    entrant = models.ForeignKey(Entrant)
    extra = models.ForeignKey(Extra)
    price = models.FloatField(max_digits=65535, decimal_places=65531)
    class Meta:
        db_table = 'entrant_extra'
