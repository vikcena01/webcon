from django.db import models

# Create your models here.

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(maxlength=64)
    login = models.CharField(maxlength=32)
    passwd_hash = models.CharField(maxlength=32)
    can_write = models.BooleanField()
    last_good_login = models.DateTimeField()
    last_bad_login = models.DateTimeField()
    active = models.BooleanField()
    
    class Meta:
        db_table = 'admin'

    def get_admin_overview_url(self):
        return "/admin/admins/%s" % self.id

    def get_admin_edit_url(self):
        return self.get_admin_overview_url() + "/edit"

    def get_admin_del_url(self):
        return self.get_admin_overview_url() + "/del"

    def get_admin_activate_url(self):
        return self.get_admin_overview_url() + "/activate"

    def get_admin_block_url(self):
        return self.get_admin_overview_url() + "/block"
