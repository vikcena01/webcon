from django.db import models
from webcon.models.common import Country
from webcon.models.confs import Room, Extra

# Create your models here.

class Entrant(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    conference_id = models.ForeignKey(Conference)
    conf_cost = models.FloatField(max_digits=65535, decimal_places=65531)
    arrived = models.DateTimeField()
    notes = models.TextField()
    conf_rating = models.SmallIntegerField()
    conf_comment = models.TextField()
    room = models.ForeignKey(Room)

    class Meta:
        db_table = 'entrant'



class EntrantExtra(models.Model):
    entrant = models.ForeignKey(Entrant)
    extra = models.ForeignKey(Extra)
    cost = models.FloatField(max_digits=65535, decimal_places=65531)
    class Meta:
        db_table = 'entrant_extra'
