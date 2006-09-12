#!/usr/bin/python

from random import random
from gen_resources import *
from webcon.common.models import Country, Address
from webcon.confs.models import Conference, Contractor
from datetime import *

counter = 0

for name in conf_names:
    c = Conference()
    c.name = name
    c.description = get_conf_desc(c.name)
    cont = Contractor()
    cont.name = "Kontrahent %i" % (counter+1)
    cont.phone = "(12) 61122609"
    cont.email = "kontrahent%i@deoman.com" % (counter+1)
    cont.account = "1234567890-98654"
    cont.address = get_address()
    cont.save()
    c.contractor = cont
    c.start_date = datetime.now()
    c.end_date = datetime.now()
    c.nights = 5
    c.price = 500
    c.cost = 400
    if counter % 2:
        c.active = True
    else:
        c.active = False
    c.address = get_address()
    c.save()
    
#    h.standard = (int)(random()*5)+1
#    h.address = a
#    h.save()
    
    counter += 1
