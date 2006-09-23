
from webcon.imports import *

#from django.db import IntegrityError
from psycopg import IntegrityError
import md5

MODULE = 'user'
SUBMODULE = 'users'
TPLPATH = MODULE+'/'+SUBMODULE
BASEPATH = '/'+MODULE+'/'+SUBMODULE

vars = { 'basepath': BASEPATH }

@user_log
def index(request):
    user_id = (request.session['user'].id or 0);
    if user_id: 
        user = get_object_or_404(User, pk=user_id)
        if user:
            vars['user'] = user
            return render(TPLPATH+'/index.html', request, vars)
        
    return HttpResponseRedirect("/login")



    