# Create your views here.
from webcon.admins.decorators import admin_logged, user_logged
from webcon.confs.models import Conference
from webcon.common.helpers import render

@user_logged
def index(request):
    confs = Conference.objects.all().order_by('name')
    # countries = Country.objects.order_by('name')
    #for h in hotels:
    #    h.tmp_country = [c.name for c in countries if c.id == h.country_id][0]
    #    h.tmp_stars = range(h.standard)
    vars = {'confs': confs}
    return render('confs/confs_index.html', request, vars)

