# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
#from django.db.models.Model import DoesNotExist
from webcon.users.models import User
from webcon.entrants.models import Entrant
from datetime import datetime
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
                    request.session['user_last_login'] = entrant.last_login
                    request.session['user_type'] = 'entrant'
                    request.session['user_fullname'] = entrant.firstname+' '+entrant.lastname
                    request.session['user_login'] = entrant.email
                    return HttpResponseRedirect("/entrant/summary/")
            except Entrant.DoesNotExist:
                pass
            return render_to_response('auth/auth_login.html', {'POST': request.POST, 'error': 'Niepoprawny login i/lub has³o!'})
        else:
            # wiec moze admin?
            try:
                user = User.objects.get(login__exact=login)
                if user.passwd_hash == passwd_hash:
                    request.session['user_id'] = user.id
                    request.session['user_last_login'] = user.last_login
                    request.session['user_login'] = user.login
                    if user.role == 1:
                        request.session['user_type'] = 'normal'
                        request.session['user_perm'] = { 'r': True, 'w': False }
                    else:
                        request.session['user_type'] = 'admin'
                        request.session['user_perm'] = { 'r': True, 'w': True }
                    request.session['user_fullname'] = user.fullname
                    # request.session['user_email'] = entrant.email
                    # zaktualizujmy last_login
                    user.last_login = datetime.now()
                    user.save()
                    return HttpResponseRedirect("/hotels/")
                
            except User.DoesNotExist:
                pass
            
            return render_to_response('auth/auth_login.html', {'POST': request.POST, 'error': 'Niepoprawny login i/lub has³o!'})
        
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


