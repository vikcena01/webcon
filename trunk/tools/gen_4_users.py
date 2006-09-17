#!/usr/bin/python

from webcon.imports import *
# from datetime import *
import md5
# from random import random
from webcon.tools.gen_resources import *


for i in range(500):
    u = User()
    u.firstname = get_firstname()
    u.lastname = get_lastname()
    u.email = get_email(u.firstname)
    u.address = get_address()
    u.phone = get_phone()
    u.birthdate = datetime(1980, 3, 4)
    u.sex = ('m', 'f')[(int)(random()*2)]
    u.registered = get_period()[0]
    u.passwd_hash = md5.new("abc").hexdigest()
    u.save()
