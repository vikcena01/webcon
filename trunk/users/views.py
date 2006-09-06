# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from webcon.admins.models import Admin
from webcon.common.models import Country
from webcon.admins.decorators import admin_logged
from webcon.common.helpers import render
from django.http import HttpResponseRedirect


@admin_logged
def index(request):
    admins = Admin.objects.all().order_by('login')
    vars = {'admins': admins}
    return render('admins/admins_index.html', request, vars)


@admin_logged
def overview(request, admin_id):
    vars = {}
#    vars['hotel_standards'] = HOTEL_STANDARDS
#    vars['countries'] = 
    admin = get_object_or_404(Admin, pk=admin_id)
    vars['admin'] = admin
    vars['admins'] = Admin.objects.all().order_by('login')
   
    return render('admins/admins_overview.html', request, vars)


@admin_logged
def edit(request, admin_id=None):
    vars = {}
    vars['admins'] = Admin.objects.all().order_by('login')
    if admin_id:
        admin = get_object_or_404(Admin, pk=admin_id)
        vars['admin'] = admin
   
    return render('admins/admins_edit.html', request, vars)



@admin_logged
def save(request):
    if request.method == 'POST':
#        hotel = Hotel.objects.get_or_create(id=(request.POST['id'] or 100), defaults={'id': None})[0]
        if request.POST['id']:
            hotel = get_object_or_404(Hotel, pk=request.POST['id'])
        else:
            hotel = Hotel()
#        return HttpResponse(str(request.POST))
        hotel.name = request.POST['name']
        hotel.standard = request.POST['standard']
        hotel.city = request.POST['city']
        hotel.address = request.POST['address']
        hotel.country_id = request.POST['country']
        hotel.description = request.POST['desc']
        hotel.save()
        return HttpResponseRedirect("/hotels/%s" % hotel.id)
    else:
        return HttpResponseRedirect("/hotels/")


@admin_logged
def delete(request, admin_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    hotel.delete()
    return HttpResponseRedirect("/hotels/")
