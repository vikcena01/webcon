# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from webcon.admin.admins.models import Admin
from webcon.common.models import Country
from webcon.admin.admins.decorators import admin_can_write
from webcon.common.helpers import render
from django.http import HttpResponseRedirect,HttpResponse
#from django.db import IntegrityError
from psycopg import IntegrityError
import md5

MODULE = 'admin'
SUBMODULE = 'admins'


@admin_can_write
def index(request):
    admins = Admin.objects.all().order_by('login')
    vars = {'admins': admins}
    return render(MODULE+'/'+SUBMODULE+'/index.html', request, vars)


@admin_can_write
def overview(request, admin_id):
    vars = {}
#    vars['hotel_standards'] = HOTEL_STANDARDS
#    vars['countries'] = 
    admin = get_object_or_404(Admin, pk=admin_id)
    # user.tmp_role = {1:'Zwyk³y u¿ytkownik', 2:'Administrator'}[user.role]
    vars['admin'] = admin
    # vars['admins'] = User.objects.all().order_by('login')
   
    return render(MODULE+'/'+SUBMODULE+'/overview.html', request, vars)


@admin_can_write
def edit(request, user_id=None):
    vars = {}
    vars['users'] = User.objects.all().order_by('login')
    if user_id:
        user = get_object_or_404(User, pk=user_id)
        vars['user'] = user
   
    return render(MODULE+'/'+SUBMODULE+'/edit.html', request, vars)



@admin_can_write
def save(request):
    if request.method == 'POST':
#        hotel = Hotel.objects.get_or_create(id=(request.POST['id'] or 100), defaults={'id': None})[0]
        if request.POST['id']:
            user = get_object_or_404(User, pk=request.POST['id'])
        else:
            user = User()
#        return HttpResponse(str(request.POST))
        user.fullname = request.POST['fullname']
        user.login = request.POST['login']
        user.role = request.POST['role']
        user.passwd_hash = passwd_hash = md5.new(request.POST['pass1']).hexdigest()
        try:
            user.save()
        except IntegrityError:
            return HttpResponse("user o podanym loginie juz istnieje!")
        return HttpResponseRedirect(MODULE+'/'+SUBMODULE+"/%s" % user.id)
    else:
        return HttpResponseRedirect(MODULE+'/'+SUBMODULE)


@admin_can_write
def delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return HttpResponseRedirect(MODULE+'/'+SUBMODULE)
