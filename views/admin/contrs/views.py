
from webcon.imports import *

MODULE = 'admin'
SUBMODULE = 'contrs'
TPLPATH = MODULE+'/'+SUBMODULE
BASEPATH = '/'+MODULE+'/'+SUBMODULE

vars = { 'basepath': BASEPATH }


@admin_can_read
def index(request):
    conts = Contractor.objects.all().order_by('name')
    # countries = Country.objects.order_by('name')
    # for h in hotels:
    #    h.tmp_stars = range(h.standard)
    vars['contractors'] = conts
    return render(TPLPATH+'/index.html', request, vars)


@admin_can_read
def overview(request, contr_id):
    cont = get_object_or_404(Contractor, pk=contr_id)
    # hotel.tmp_stars = range(hotel.standard)
    vars['contractor'] = cont
    vars['contractors'] = Contractor.objects.all().order_by('name')
   
    return render(TPLPATH+'/overview.html', request, vars)


@admin_can_write
def edit(request, contr_id=None):
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
def delete(request, contr_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    hotel.delete()
    return HttpResponseRedirect(BASEPATH)
