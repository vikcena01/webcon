
from webcon.imports import *
from datetime import datetime
import md5
from django.db import connection

def login(request):
    # blabla
    if request.method == 'POST':
        login = request.POST.get('login', '').strip()
        passwd_hash = md5.new(request.POST['pass']).hexdigest()
        
        if '@' in login:
            # sprobojmy zalogowac uczestnika
            cursor = connection.cursor()
            cursor.execute("SELECT auth_user(%s,%s) AS id", [login,passwd_hash])
            row = cursor.fetchone()
            id = row[0]
            if id >= 0:
                user = User.objects.get(pk=id)
                request.session['user'] = user
                return HttpResponseRedirect("/user/")

            return render_to_response('auth/auth_login.html', {'POST': request.POST, 'error': 'Niepoprawny login i/lub has³o!'})
        else:
            # wiec moze admin?
            cursor = connection.cursor()
            cursor.execute("SELECT auth_admin(%s,%s) AS id", [login,passwd_hash])
            row = cursor.fetchone()
            id = row[0]
            if id >= 0:
                admin = Admin.objects.get(pk=id)
                request.session['admin'] = admin
                request.session['user'] = admin
                return HttpResponseRedirect("/admin/confs/")
                
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


