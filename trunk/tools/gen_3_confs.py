#!/usr/bin/python

from random import random
from gen_resources import *
from webcon.common.models import Country, Address
from webcon.confs.models import Conference, Contractor
from datetime import *

contractors = Contractor.objects.all()

counter = 0

for name in conf_names:
    c = Conference()
    c.name = name
    c.description = get_conf_desc(c.name)
    c.contractor = contractors[(int)(random()*len(contractors))]
    (start, stop, nights) = get_period()
    c.start_date = start
    c.end_date = stop
    c.nights = nights
    c.price = get_price()*10
    c.cost = (int)(c.price*0.8)
    if counter % 2:
        c.active = True
    else:
        c.active = False
    c.address = get_address()
    c.reg_deadline = start + timedelta(-7)
    c.save()
  
    counter += 1
