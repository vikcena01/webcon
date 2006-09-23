
from webcon.imports import *

#from django.db import IntegrityError
from psycopg import IntegrityError, ProgrammingError
import md5

MODULE = 'admin'
SUBMODULE = 'admins'
TPLPATH = MODULE+'/'+SUBMODULE
BASEPATH = '/'+MODULE+'/'+SUBMODULE

# vars = { 'basepath': BASEPATH }

@admin_can_write
def index(request):
    admins = Admin.objects.all().order_by('login')
    vars = { 'basepath': BASEPATH }
    vars['admins'] = admins
    return render(TPLPATH+'/index.html', request, vars)


@admin_can_write
def overview(request, admin_id):
    admin = get_object_or_404(Admin, pk=admin_id)
    vars = { 'basepath': BASEPATH }
    vars['admin'] = admin
   
    return render(TPLPATH+'/overview.html', request, vars)


def render_edit(request,admin,vars={ 'basepath': BASEPATH } ):
    vars['admin'] = admin
    return render(TPLPATH+'/edit.html', request, vars)

@admin_can_write
def edit(request, admin_id=None):
    # vars['users'] = User.objects.all().order_by('login')
    if admin_id:
        admin = get_object_or_404(Admin, pk=admin_id)
    else:
        admin = Admin()
    return render_edit(request, admin)
  
#    return render(TPLPATH+'/edit.html', request, vars)



@admin_can_write
def save(request):
    if request.method == 'POST':
        if request.POST['id'].strip():
            admin = get_object_or_404(Admin, pk=request.POST['id'])
        else:
            admin = Admin()

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
        except (IntegrityError, ProgrammingError), e:
            from django.db import connection
            connection._rollback()
            vars = { 'basepath': BASEPATH }
            vars['error_msg'] = integrity_get_message(str(e))
            return render_edit(request,admin,vars)
        
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
