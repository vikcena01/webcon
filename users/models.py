from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(maxlength=64)
    login = models.CharField(maxlength=32)
    passwd_hash = models.CharField(maxlength=32)
    role = models.SmallIntegerField()
    last_login = models.DateTimeField()
    
    class Meta:
        db_table = 'sysuser'

    def get_absolute_url(self):
        return "/users/%s" % self.id
