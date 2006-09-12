#!/usr/bin/python

from random import random
from gen_resources import *
from webcon.common.models import Country, Address
from webcon.hotels.models import Hotel


for name in hotel_names:
    h = Hotel()
    h.name = name
    h.description = get_hotel_desc(h.name)
    h.standard = (int)(random()*5)+1
    h.address = get_address()
    h.save()
