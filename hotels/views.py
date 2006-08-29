# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from webcon.hotels.models import Hotel
from webcon.common.models import Country
from webcon.auth.decorators import admin_logged
from webcon.common.helpers import render

HOTEL_STANDARDS = [
   {'value':1, 'stars':'*'},
   {'value':2, 'stars':'**'},
   {'value':3, 'stars':'***'},
   {'value':4, 'stars':'****'},
   {'value':5, 'stars':'*****'}
]

@admin_logged
def index(request):
    hotels = Hotel.objects.all().order_by('name')
    vars = {'session': request.session, 'hotels': hotels}
    return render('hotels/hotels_index.html', request, vars)


@admin_logged
def details(request, hotel_id):
    vars = {}
    
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    if request.method == 'POST':
        hotel.name = request.POST['name']
        hotel.standard = request.POST['standard']
        hotel.city = request.POST['city']
        hotel.address = request.POST['address']
        hotel.country_id = request.POST['country']
        hotel.desc = request.POST['desc']
        hotel.save()
        vars['msg_ok'] = 'Informacje o hotelu zosta³y zaktualizowane'
        
    vars['hotel'] = hotel
    vars['hotel_standards'] = HOTEL_STANDARDS
    vars['countries'] = Country.objects.order_by('name')
    
    return render('hotels/hotels_details.html', request, vars)


@admin_logged
def new(request):
    vars = {}
    vars['hotel_standards'] = HOTEL_STANDARDS
    vars['countries'] = Country.objects.order_by('name')
    
    return render('hotels/hotels_details.html', request, vars)

