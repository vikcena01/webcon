#!/usr/bin/python

from random import random
from gen_resources import *
# from webcon.common.models import Country, Address
from webcon.confs.models import Contractor


for i in range(10):
    cont = Contractor()
    cont.name = "Kontrahent %i" % (i+1)
    cont.phone = get_phone()
    cont.email = get_email()
    cont.account = get_account()
    cont.address = get_address()
    cont.save()
