
from webcon.imports import *

#from django.db import IntegrityError
from psycopg import IntegrityError
import md5

MODULE = 'admin'
SUBMODULE = 'admins'
TPLPATH = MODULE+'/'+SUBMODULE
BASEPATH = '/'+MODULE+'/'+SUBMODULE

vars = { 'basepath': BASEPATH }

@admin_can_write
def index(request):
    admins = Admin.objects.all().order_by('login')
    vars['admins'] = admins
    return render(TPLPATH+'/index.html', request, vars)


@admin_can_write
def overview(request, admin_id):
#    vars['hotel_standards'] = HOTEL_STANDARDS
#    vars['countries'] = 
    admin = get_object_or_404(Admin, pk=admin_id)
    # user.tmp_role = {1:'Zwyk�y u�ytkownik', 2:'Administrator'}[user.role]
    vars['admin'] = admin
    # vars['admins'] = User.objects.all().order_by('login')
   
    return render(TPLPATH+'/overview.html', request, vars)


@admin_can_write
def edit(request, admin_id=None):
    # vars['users'] = User.objects.all().order_by('login')
    if admin_id:
        admin = get_object_or_404(Admin, pk=admin_id)
        vars['admin'] = admin
   
    return render(TPLPATH+'/edit.html', request, vars)



@admin_can_write
def save(request):
    if request.method == 'POST':
#        hotel = Hotel.objects.get_or_create(id=(request.POST['id'] or 100), defaults={'id': None})[0]
        if request.POST['id']:
            admin = get_object_or_404(Admin, pk=request.POST['id'])
        else:
            admin = Admin()
#        return HttpResponse(str(request.POST))
        admin.fullname = request.POST['fullname']
        admin.login = request.POST['login']
        if request.POST.get('can_write', '0') == '1':
            admin.can_write = True
        else:
            admin.can_write = False
            
        # user.role = request.POST['role']
        admin.passwd_hash = md5.new(request.POST['pass1']).hexdigest()
        try:
            admin.save()
        except IntegrityError:
            return HttpResponse("admin o podanym loginie juz istnieje!")
        return HttpResponseRedirect(BASEPATH+"/%s" % admin.id)
    else:
        return HttpResponseRedirect(BASEPATH)


@admin_can_write
def delete(request, admin_id):
    admin = get_object_or_404(Admin, pk=admin_id)
    admin.delete()
    return HttpResponseRedirect(BASEPATH)

@admin_can_write
def block(request, admin_id):
    admin = get_object_or_404(Admin, pk=admin_id)
    admin.active = False
    admin.save()
    return HttpResponseRedirect(BASEPATH+"/%s" % admin.id)

@admin_can_write
def activate(request, admin_id):
    admin = get_object_or_404(Admin, pk=admin_id)
    admin.active = True
    admin.save()
    return HttpResponseRedirect(BASEPATH+"/%s" % admin.id)