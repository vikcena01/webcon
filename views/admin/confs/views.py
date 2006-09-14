
from webcon.imports import *

MODULE = 'admin'
SUBMODULE = 'confs'
TPLPATH = MODULE+'/'+SUBMODULE
BASEPATH = '/'+MODULE+'/'+SUBMODULE

vars = { 'basepath': BASEPATH }

@admin_can_read
def index(request):
    confs = Conference.objects.all().order_by('name')
    # countries = Country.objects.order_by('name')
    #for h in hotels:
    #    h.tmp_country = [c.name for c in countries if c.id == h.country_id][0]
    #    h.tmp_stars = range(h.standard)
    vars['confs'] = confs
    return render(TPLPATH+'/index.html', request, vars)

