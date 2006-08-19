from django.db import models
from webcon.common.models import Country

# Create your models here.

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(maxlength=64)
    description = models.TextField()
    type = models.SmallIntegerField()
    country = models.ForeignKey(Country, db_column='country')
    city = models.CharField(maxlength=64)
    address = models.CharField(maxlength=256)
    standard = models.SmallIntegerField()
    class Meta:
        db_table = 'hotel'
        
    def str(self):
        return name + ' (' + '*' * standard + ')'
    
    def get_absolute_url(self):
        return '/hotels/'+self.id
