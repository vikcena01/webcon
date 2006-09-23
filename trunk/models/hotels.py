from django.db import models
from webcon.models.common import Address

# Create your models here.

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(maxlength=64)
    description = models.TextField()
    type = models.SmallIntegerField()
    address = models.ForeignKey(Address)
    standard = models.SmallIntegerField()

    class Meta:
        db_table = 'hotel'
        
    def str(self):
        return self.name + ' (' + '*' * self.standard + ')'

    def get_name(self):
        return self.str()
    