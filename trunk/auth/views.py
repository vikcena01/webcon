# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
#from django.db.models.Model import DoesNotExist
from webcon.auth.models import Sysuser
from webcon.entrants.models import Entrant
# from django.db import models
import md5


def login(request):
    # blabla
    if request.method == 'POST':
        login = request.POST.get('login', '').strip()
        passwd_hash = md5.new(request.POST['pass']).hexdigest()
        
        if '@' in login:
            # sprobojmy zalogowac uczestnika
            try:
                entrant = Entrant.objects.get(email__exact=login)
                if entrant.passwd_hash == passwd_hash:
                    request.session['user_id'] = entrant.id
                    request.session['user_type'] = 'entrant'
                    request.session['user_fullname'] = entrant.firstname+' '+entrant.lastname
                    request.session['user_email'] = entrant.email
                    return HttpResponseRedirect("/entrant/summary/")
            except Entrant.DoesNotExist:
                pass
            return render_to_response('auth/auth_login.html', {'POST': request.POST, 'error': 'Niepoprawny login i/lub has�o!'})
        else:
            # wiec moze admin?
            try:
                admin = Sysuser.objects.get(login__exact=login)
                if admin.passwd_hash == passwd_hash:
                    request.session['user_id'] = admin.id
                    request.session['user_type'] = 'admin'
                    if admin.role == 1:
                        request.session['user_perm'] = { 'r': True, 'w': False }
                    else:
                        request.session['user_perm'] = { 'r': True, 'w': True }
                    request.session['user_fullname'] = admin.fullname
                    # request.session['user_email'] = entrant.email
                    return HttpResponseRedirect("/hotels/")
                
            except Sysuser.DoesNotExist:
                pass
            
            return render_to_response('auth/auth_login.html', {'POST': request.POST, 'error': 'Niepoprawny login i/lub has�o!'})
        
    else:
        return render_to_response('auth/auth_login.html')


def logout(request):
    # blabla
    try:
        del request.session['user_id']
        del request.session['user_type']
        del request.session['user_fullname']
        del request.session['user_perm']
        del request.session['user_email']
    except KeyError:
        pass
    
    return HttpResponseRedirect("/login")


