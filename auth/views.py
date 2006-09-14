# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
#from django.db.models.Model import DoesNotExist
from webcon.admin.admins.models import Admin
from webcon.admin.users.models import User
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
                user = User.objects.get(email__exact=login)
                if user.passwd_hash == passwd_hash:
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
                admin = Admin.objects.get(login__exact=login)
                if admin.passwd_hash == passwd_hash:
                    request.session['admin'] = admin
                    request.session['user'] = admin
                    # request.session['user_email'] = entrant.email
                    # zaktualizujmy last_login
                    admin.last_login = datetime.now()
                    admin.save()
                    return HttpResponseRedirect("/hotels/")
                
            except User.DoesNotExist:
                pass
            
            return render_to_response('auth/auth_login.html', {'POST': request.POST, 'error': 'Niepoprawny login i/lub has³o!'})
        
    else:
        return render_to_response('auth/auth_login.html')


def logout(request):
    # blabla
    try:
        del request.session['user']
        del request.session['admin']
    except KeyError:
        pass
    
    return HttpResponseRedirect("/login")


