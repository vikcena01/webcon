
from webcon.imports import *

#from django.db import IntegrityError
from psycopg import IntegrityError
import md5

MODULE = 'user'
TPLPATH = MODULE
BASEPATH = '/'+MODULE

vars = { 'basepath': BASEPATH }

@user_log
def index(request):
    user_id = request.session['user'].id
    user = get_object_or_404(User, pk=user_id)
    vars['user'] = user
    
    vars['sex_types'] = [('K','Kobieta'),('M','Mê¿czyzna')]
    vars['countries'] = [(c.id, c.name) for c in Country.objects.order_by('name')]
    
    return render(TPLPATH+'/index.html', request, vars)





    