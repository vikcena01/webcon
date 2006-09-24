from django.db import models
from webcon.models.common import Address

# Create your models here.

class Hotel(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(maxlength=64,default="")
    description = models.TextField(default="")
    type = models.SmallIntegerField(default=1)
    address = models.ForeignKey(Address)
    standard = models.SmallIntegerField(default=1)

    class Meta:
        db_table = 'hotel'
        
    def str(self):
        return self.name + ' (' + '*' * self.standard + ')'

    def get_name(self):
        return self.str()
    