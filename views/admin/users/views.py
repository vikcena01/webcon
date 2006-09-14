# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from webcon.models.admins import Admin
from webcon.common.models import Country
from webcon.admins.decorators import admin_can_write
from webcon.common.helpers import render
from django.http import HttpResponseRedirect,HttpResponse
#from django.db import IntegrityError
from psycopg import IntegrityError

import md5


@admin_can_write
def index(request):
    admins = Admin.objects.all().order_by('login')
    vars = {'admins': admins}
    return render('users/users_index.html', request, vars)


@admin_can_write
def overview(request, admin_id):
    vars = {}
#    vars['hotel_standards'] = HOTEL_STANDARDS
#    vars['countries'] = 
    user = get_object_or_404(User, pk=user_id)
    user.tmp_role = {1:'Zwyk³y u¿ytkownik', 2:'Administrator'}[user.role]
    vars['user'] = user
    vars['users'] = User.objects.all().order_by('login')
   
    return render('users/users_overview.html', request, vars)


@admin_can_write
def edit(request, user_id=None):
    vars = {}
    vars['users'] = User.objects.all().order_by('login')
    if user_id:
        user = get_object_or_404(User, pk=user_id)
        vars['user'] = user
   
    return render('users/users_edit.html', request, vars)



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
        return HttpResponseRedirect("/users/%s" % user.id)
    else:
        return HttpResponseRedirect("/users/")


@admin_can_write
def delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return HttpResponseRedirect("/users/")
