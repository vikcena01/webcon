
from webcon.imports import *

MODULE = 'admin'
SUBMODULE = 'hotels'
TPLPATH = MODULE+'/'+SUBMODULE
BASEPATH = '/'+MODULE+'/'+SUBMODULE

vars = { 'basepath': BASEPATH }

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
    vars['hotels'] = hotels
    return render(TPLPATH+'/index.html', request, vars)


@admin_can_read
def overview(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    hotel.tmp_stars = range(hotel.standard)
    vars['hotel'] = hotel
    vars['hotels'] = Hotel.objects.all().order_by('name')
   
    return render(TPLPATH+'/overview.html', request, vars)


@admin_can_write
def edit(request, hotel_id=None):
    vars['hotel_standards'] = HOTEL_STANDARDS
    vars['countries'] = Country.objects.order_by('name')
    vars['hotels'] = Hotel.objects.all().order_by('name')
    if hotel_id:
        hotel = get_object_or_404(Hotel, pk=hotel_id)
        vars['hotel'] = hotel
   
    return render(TPLPATH+'/edit.html', request, vars)



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
        
        return HttpResponseRedirect(BASEPATH+"/%s" % hotel.id)
    else:
        return HttpResponseRedirect(BASEPATH)


@admin_can_write
def delete(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    hotel.delete()
    return HttpResponseRedirect(BASEPATH)
