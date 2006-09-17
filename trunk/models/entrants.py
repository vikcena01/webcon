from django.db import models
from webcon.models.common import Country
from webcon.models.confs import Room, Extra

# Create your models here.

class Entrant(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    conference_id = models.ForeignKey(Conference)
    conf_price = models.FloatField(max_digits=65535, decimal_places=65531)
    arrived = models.DateTimeField()
    notes = models.TextField()
    conf_rating = models.SmallIntegerField()
    conf_comment = models.TextField()
    room = models.ForeignKey(Room)
    nights = models.SmallIntegerField()

    def get_admin_overview_url(self):
        return "/admin/entr/%s" % self.id

    def get_admin_edit_url(self):
        return self.get_admin_overview_url() + "edit"

    def get_admin_del_url(self):
        return self.get_admin_overview_url() + "del"

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
