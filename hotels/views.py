# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from webcon.hotels.models import Hotel
from webcon.auth.decorators import admin_logged

@admin_logged
def index(request):
    hotels = Hotel.objects.all().order_by('name')
    return render_to_response('hotels/hotels_index.html', {'session': request.session, 'hotels': hotels})
#    return HttpResponse("Hello, world from hotels.")

@admin_logged
def details(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    return render_to_response('hotels/hotels_details.html', {'session': request.session, 'hotel': hotel})
#    return HttpResponse("Hello, world from hotels.")

@admin_logged
def new(request):
    return render_to_response('hotels/hotels_details.html', {'session': request.session})

