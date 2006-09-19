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

    page, sort_by, sort_order, words = get_list_params(request, 'users')
    
    # filtrowanie 
    
    if words:
        cond = Q()
        for w in words:
            subcond = Q()
            subcond |= Q(firstname__istartswith=w)
            subcond |= Q(lastname__istartswith=w)
            subcond |= Q(email__icontains=w)
            cond &= subcond
        q = User.objects.filter(cond)
    else:
        q = User.objects.all()


    # pager
    
    count = q.count()
    pages = count / elements_per_page
    offset = page * elements_per_page
    if count % elements_per_page > 0:
        pages += 1

    vars['offset'] = offset
    if pages > 1:
        vars['pages'] = range(pages)
    else:
        vars['pages'] = None
    vars['page'] = page
        
    # sortowanie
    
    if sort_by == 'name' or not sort_by:
        q = q.order_by(sort_order+'lastname', 'firstname')
    elif sort_by == 'phone':
        q = q.order_by(sort_order+'phone')
    elif sort_by == 'email':
        q = q.order_by(sort_order+'email')
    
    # pobranie danych
    
    users = q[offset:offset+elements_per_page]
    vars['users'] = users
    
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
