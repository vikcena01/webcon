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
