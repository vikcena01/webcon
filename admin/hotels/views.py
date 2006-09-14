# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from webcon.admin.hotels.models import Hotel
from webcon.common.models import Country, Address
from webcon.admin.admins.decorators import admin_can_read, admin_can_write
from webcon.common.helpers import render
from django.http import HttpResponseRedirect

HOTEL_STANDARDS = [
   {'value':1, 'stars':'*'},
   {'value':2, 'stars':'**'},
   {'value':3, 'stars':'***'},
   {'value':4, 'stars':'****'},
   {'value':5, 'stars':'*****'}
]

@admin_can_read
def index(request):
    hotels = Hotel.objects.all().order_by('name')
    countries = Country.objects.order_by('name')
    for h in hotels:
        h.tmp_stars = range(h.standard)
    vars = {'hotels': hotels}
    return render('hotels/hotels_index.html', request, vars)


@admin_can_read
def overview(request, hotel_id):
    vars = {}
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    hotel.tmp_stars = range(hotel.standard)
    vars['hotel'] = hotel
    vars['hotels'] = Hotel.objects.all().order_by('name')
   
    return render('hotels/hotels_overview.html', request, vars)


@admin_can_write
def edit(request, hotel_id=None):
    vars = {}
    vars['hotel_standards'] = HOTEL_STANDARDS
    vars['countries'] = Country.objects.order_by('name')
    vars['hotels'] = Hotel.objects.all().order_by('name')
    if hotel_id:
        hotel = get_object_or_404(Hotel, pk=hotel_id)
        vars['hotel'] = hotel
   
    return render('hotels/hotels_edit.html', request, vars)



@admin_can_write
def save(request):
    if request.method == 'POST':
#        hotel = Hotel.objects.get_or_create(id=(request.POST['id'] or 100), defaults={'id': None})[0]
        if request.POST['id']:
            hotel = get_object_or_404(Hotel, pk=request.POST['id'])
        else:
            hotel = Hotel()
#        return HttpResponse(str(request.POST))
        hotel.address.city = request.POST['city']
        hotel.address.address = request.POST['address']
        hotel.address.country_id = request.POST['country']
        hotel.address.save()

        hotel.name = request.POST['name']
        hotel.standard = request.POST['standard']
        hotel.description = request.POST['desc']
        hotel.save()
        
        return HttpResponseRedirect("/hotels/%s" % hotel.id)
    else:
        return HttpResponseRedirect("/hotels/")


@admin_can_write
def delete(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    hotel.delete()
    return HttpResponseRedirect("/hotels/")
