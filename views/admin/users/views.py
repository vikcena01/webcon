# Create your views here.

from webcon.imports import *

#from django.db import IntegrityError
from psycopg import IntegrityError

import md5

MODULE = 'admin'
SUBMODULE = 'users'
TPLPATH = MODULE+'/'+SUBMODULE
BASEPATH = '/'+MODULE+'/'+SUBMODULE
elements_per_page = 25
vars = { 'basepath': BASEPATH }


@admin_can_write
def index(request):
    page = int(request.GET.get('page', 0))
    offset = page * elements_per_page
    count = User.objects.all().count()
    pages = count / elements_per_page
    if count % elements_per_page > 0:
        pages += 1
    users = User.objects.all().order_by('lastname', 'firstname')[offset:offset+elements_per_page]
    vars['users'] = users
    vars['offset'] = offset
    vars['pages'] = range(pages)
    vars['page'] = page
    # vars['']
    return render(TPLPATH+'/index.html', request, vars)


@admin_can_write
def overview(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    vars['user'] = user
#    vars['users'] = User.objects.all().order_by('login')
   
    return render(TPLPATH+'/overview.html', request, vars)


@admin_can_write
def edit(request, user_id=None):
    # vars['users'] = User.objects.all().order_by('login')
    if user_id:
        user = get_object_or_404(User, pk=user_id)
    else:
        user = None
    
    vars['user'] = user
   
    return render(TPLPATH+'/edit.html', request, vars)



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
#        user.role = request.POST['role']
        user.passwd_hash = passwd_hash = md5.new(request.POST['pass1']).hexdigest()
        try:
            user.save()
        except IntegrityError:
            return HttpResponse("user o podanym loginie juz istnieje!")
        return HttpResponseRedirect(BASEPATH+"/%s" % user.id)
    else:
        return HttpResponseRedirect(BASEPATH)


@admin_can_write
def delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return HttpResponseRedirect(BASEPATH)
