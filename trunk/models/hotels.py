from django.db import models
from webcon.models.m_common import Country, Address

# Create your models here.

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(maxlength=64)
    description = models.TextField()
    type = models.SmallIntegerField()
    address = models.ForeignKey(Address)
    # city = models.CharField(maxlength=64)
    # address = models.CharField(maxlength=256)
    standard = models.SmallIntegerField()
    class Meta:
        db_table = 'hotel'
        
    def str(self):
        return self.name + ' (' + '*' * self.standard + ')'
    
    def get_admin_url(self):
        return "/admin/hotels/%s" % self.id

    def get_user_url(self):
        return "/user/hotels/%s" % self.id

    def get_name(self):
        return self.str()
    