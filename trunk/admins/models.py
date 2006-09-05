from django.db import models

# Create your models here.

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(maxlength=64)
    login = models.CharField(maxlength=32)
    passwd_hash = models.CharField(maxlength=32)
    role = models.SmallIntegerField()
    class Meta:
        db_table = 'sysuser'

    def get_absolute_url(self):
        return "/admins/%s" % self.id
