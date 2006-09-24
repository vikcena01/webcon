
from webcon.imports import *
#from django.db import IntegrityError
from psycopg import IntegrityError
import md5
from datetime import datetime

MODULE = 'user'
TPLPATH = MODULE
BASEPATH = '/'+MODULE

vars = { 'basepath': BASEPATH }

@user_log
def index(request):
    user_id = request.session['user'].id
    user = get_object_or_404(User, pk=user_id)
    vars['user'] = user
    
    vars['sex_types'] = [('k','Kobieta'),('m','Mê¿czyzna')]
    vars['countries'] = [(c.id, c.name) for c in Country.objects.order_by('name')]
    
    return render(TPLPATH+'/index.html', request, vars)

@user_log
def save(request):
    msg = [{'color':'#CC0000','content':'Stare has³o niepoprawne!'}, {'color':'#CC0000','content':'Podaj dwa razy takie samo has³o!'},{'color':'#0000CC','content':'Zmiany zapisane'}]
    vars['sex_types'] = [('k','Kobieta'),('m','Mê¿czyzna')]
    vars['countries'] = [(c.id, c.name) for c in Country.objects.order_by('name')]
    
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.POST['id'])
        vars['user'] = user
        
        if request.POST['old_pass']:
            passwd_hash = md5.new(request.POST['old_pass']).hexdigest()
            if user.passwd_hash != passwd_hash:
                vars['msg'] = msg[0]
                return render(TPLPATH+'/index.html', request, vars)
            
        if (request.POST['new_pass'] or request.POST['new_pass2']) and request.POST['new_pass'] != request.POST['new_pass2']:
            vars['msg'] = msg[1]
            return render(TPLPATH+'/index.html', request, vars)
        
        
        user.address.city       = request.POST['city']
        user.address.address    = request.POST['address']
        user.address.country_id = request.POST['country']
        user.address.save()
        
        user.firstname = request.POST['firstname']
        user.lastname  = request.POST['lastname']
        user.sex       = request.POST['sex']
        user.phone     = request.POST['phone']
        user.email     = request.POST['email']
        user.birthdate = datetime(int(request.POST['birthdate_year']), int(request.POST['birthdate_month']), int(request.POST['birthdate_day']))
        user.save()
        
        vars['user'] = user
        vars['msg'] = msg[2]
        return render(TPLPATH+'/index.html', request, vars)
    
    else:
        vars['user'] = user
        return render(TPLPATH+'/index.html', request, vars)
        
@user_log
def extra(request):
    return




    