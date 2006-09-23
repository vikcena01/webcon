
from webcon.imports import *

MODULE = 'admin'
SUBMODULE = 'hotels'
TPLPATH = MODULE+'/'+SUBMODULE
BASEPATH = '/'+MODULE+'/'+SUBMODULE
elements_per_page = 25
vars = { 'basepath': BASEPATH }

HOTEL_STANDARDS = [
   (1, '*'),
   (2, '**'),
   (3, '***'),
   (4, '****'),
   (5, '*****')
]

@admin_can_read
def index(request):

    page, sort_by, sort_order, words = get_list_params(request, 'hotels')

    # filtrowanie 
    
    if words:
        cond = Q()
        for w in words:
            subcond = Q()
            subcond |= Q(name__icontains=w)
            subcond |= Q(address__city__istartswith=w)
            subcond |= Q(address__country__name__icontains=w)
            cond &= subcond
        q = Hotel.objects.filter(cond)
    else:
        q = Hotel.objects.all()

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
        q = q.order_by(sort_order+'name')
    elif sort_by == 'standard':
        q = q.order_by(sort_order+'standard')
    
    # pobranie danych
    
    hotels = q[offset:offset+elements_per_page]

    for h in hotels:
        h.tmp_stars = range(h.standard)
    vars['hotels'] = hotels
    
    return render(TPLPATH+'/index.html', request, vars)


@admin_can_read
def overview(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    hotel.tmp_stars = range(hotel.standard)
    vars['hotel'] = hotel
#    vars['hotels'] = Hotel.objects.all().order_by('name')
   
    return render(TPLPATH+'/overview.html', request, vars)


@admin_can_write
def edit(request, hotel_id=None):
    vars['hotel_standards'] = HOTEL_STANDARDS
    vars['hotel_types'] = [(1, 'Konferencyjny'), (2, 'Noclegowy')]
    vars['countries'] = [(c.id, c.name) for c in Country.objects.order_by('name')]
#    vars['hotels'] = Hotel.objects.all().order_by('name')
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
        hotel.type = int(request.POST['type'])
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
