# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from webcon.hotels.models import Hotel

def index(request):
    hotels = Hotel.objects.all().order_by('name')
    return render_to_response('hotels/hotels_index.html', {'hotels': hotels})
#    return HttpResponse("Hello, world from hotels.")

def details(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    return render_to_response('hotels/hotels_details.html', {'hotel': hotel})
#    return HttpResponse("Hello, world from hotels.")

def new(request):
    return render_to_response('hotels/hotels_ details.html')

