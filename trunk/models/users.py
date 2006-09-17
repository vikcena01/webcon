from django.db import models
from webcon.models.common import Address

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(maxlength=40)
    lastname = models.CharField(maxlength=40)
    address = models.ForeignKey(Address)
    email = models.CharField(maxlength=40)
    phone = models.CharField(maxlength=16)
    birthdate = models.DateField()
    sex = models.CharField(maxlength=1)
    passwd_hash = models.CharField(maxlength=32)
    registered = models.DateTimeField()
    last_good_login = models.DateTimeField()
    last_bad_login = models.DateTimeField()

    def fullname(self):
        return self.firstname + " " + self.lastname
    
    def get_admin_overview_url(self):
        return "/admin/users/%s" % self.id

    def get_admin_edit_url(self):
        return self.get_admin_overview_url() + "edit"

    def get_admin_del_url(self):
        return self.get_admin_overview_url() + "del"

    class Meta:
        db_table = 'user'
        
    class Admin:
        pass

