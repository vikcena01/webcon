from django.db import models
from webcon.models.common import Address

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
    
    def get_absolute_url(self):
        return "/contr/%s" % self.id

    class Meta:
        db_table = 'contractor'

