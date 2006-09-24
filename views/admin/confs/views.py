
from webcon.imports import *
from datetime import datetime
from psycopg import IntegrityError, ProgrammingError

MODULE = 'admin'
SUBMODULE = 'confs'
TPLPATH = MODULE+'/'+SUBMODULE
BASEPATH = '/'+MODULE+'/'+SUBMODULE
elements_per_page = 25


@admin_can_read
def index(request):
    actual_confs = ActualConference.objects.all().order_by('-start_date')
    comming_confs = CommingConference.objects.all().order_by('start_date')
    vars = { 'basepath': BASEPATH }
    vars['actual_confs'] = actual_confs
    vars['comming_confs'] = comming_confs
    return render(TPLPATH+'/index.html', request, vars)


@admin_can_read
def archive(request):
    vars = { 'basepath': BASEPATH }

    page, sort_by, sort_order, words = get_list_params(request, 'archive')

    # filtrowanie 
    
    if words:
        cond = Q()
        for w in words:
            subcond = Q()
            subcond |= Q(name__icontains=w)
            subcond |= Q(hotel__name__icontains=w)
            cond &= subcond
        q = ArchiveConference.objects.filter(cond)
    else:
        q = ArchiveConference.objects.all()

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
    
    q = q.order_by('-end_date')
   
    # pobranie danych
    
    confs = q[offset:offset+elements_per_page]
    vars['confs'] = confs
    return render(TPLPATH+'/archive.html', request, vars)
    

@admin_can_read
def overview(request, conf_id):
    conf = get_object_or_404(Conference, pk=conf_id)
    vars = { 'basepath': BASEPATH }
    vars['conf'] = conf
    vars['confpath'] = BASEPATH+'/%s' % conf.id
#    vars['hotels'] = Hotel.objects.all().order_by('name')
   
    return render(TPLPATH+'/overview.html', request, vars)


@admin_can_write
def close(request, conf_id):
    conf = get_object_or_404(Conference, pk=conf_id)
    conf.active = False
    conf.save()
    return HttpResponseRedirect(BASEPATH+"/%s" % conf.id)

@admin_can_write
def open(request, conf_id):
    conf = get_object_or_404(Conference, pk=conf_id)
    conf.active = True
    conf.save()
    return HttpResponseRedirect(BASEPATH+"/%s" % conf.id)


def render_edit(request,conf,vars={ 'basepath': BASEPATH } ):
    contractors = [(c.id, c.name) for c in Contractor.objects.all().order_by('name')]
    hotels = [(h.id, h.name) for h in Hotel.objects.all().filter(type=1).order_by('name')]

    vars['conf'] = conf
    vars['contractors'] = contractors
    vars['hotels'] = hotels
    vars['confpath'] = BASEPATH+'/%s' % conf.id
   
    return render(TPLPATH+'/edit.html', request, vars)    
    
    
    
@admin_can_write
def edit(request, conf_id=None):
    if conf_id:
        conf = get_object_or_404(Conference, pk=conf_id)
    else:
        conf = Conference()
    return render_edit(request,conf)
   
    # return render(TPLPATH+'/edit.html', request, vars)


@admin_can_write
def save(request):
    if request.method == 'POST':
        if request.POST['id'].strip():
            conf = get_object_or_404(Conference, pk=request.POST['id'])
        else:
            conf = Conference()
            
        conf.name = request.POST['name']
        conf.description = request.POST['desc']
        conf.cost = float(request.POST['cost'])
        conf.contractor_id = int(request.POST['contractor'])
        conf.hotel_id = int(request.POST['hotel'])
        conf.start_date = datetime(int(request.POST['start_date_year']), int(request.POST['start_date_month']), int(request.POST['start_date_day']))    
        conf.end_date = datetime(int(request.POST['end_date_year']), int(request.POST['end_date_month']), int(request.POST['end_date_day']))    
        conf.reg_deadline = datetime(int(request.POST['reg_deadline_year']), int(request.POST['reg_deadline_month']), int(request.POST['reg_deadline_day']))    
        
        try:
            conf.save()
        except (IntegrityError, ProgrammingError), e:
            from django.db import connection
            connection._rollback()
            vars = { 'basepath': BASEPATH }
            vars['error_msg'] = integrity_get_message(str(e))
            return render_edit(request,conf,vars)
            
        return HttpResponseRedirect(BASEPATH+"/%s" % conf.id)
    else:
        return HttpResponseRedirect(BASEPATH)


@admin_can_write
def delete(request, conf_id):
    conf = get_object_or_404(Conference, pk=conf_id)
    conf.delete()
    return HttpResponseRedirect(BASEPATH)



@admin_can_read
def events(request, conf_id):
    conf = get_object_or_404(Conference, pk=conf_id)
    vars = { 'basepath': BASEPATH }
    vars['confpath'] = BASEPATH+'/%s' % conf.id
    vars['conf'] = conf
    vars['events'] = Event.objects.filter(conference=conf).order_by('time')
    return render(TPLPATH+'/events.html', request, vars)


def render_event_edit(request, conf_id, event, vars = { 'basepath': BASEPATH }):       
    vars['confpath'] = BASEPATH+'/%s' % conf_id
    vars['event'] = event
    return render(TPLPATH+'/event_edit.html', request, vars)


def event_edit(request, conf_id, event_id=None):
    if event_id:
        event = Event.objects.get(pk=event_id)
    else:
        event = Event()
#        event.time = datetime
    return render_event_edit(request, conf_id, event)


@admin_can_write
def event_save(request, conf_id):
    if request.method == 'POST':
        if request.POST['id'].strip():
            event = get_object_or_404(Event, pk=request.POST['id'])
        else:
            event = Event()
            event.conference_id = conf_id
            
        event.name = request.POST['name']
        event.description = request.POST['desc']
        event.place = request.POST['place']
        event.time = datetime(int(request.POST['date_year']), int(request.POST['date_month']), int(request.POST['date_day']), int(request.POST['time_hour']), int(request.POST['time_minute']))    
        
        try:
            event.save()
        except (IntegrityError, ProgrammingError), e:
            from django.db import connection
            connection._rollback()
            vars = { 'basepath': BASEPATH}
            vars['error_msg'] = integrity_get_message(str(e))
            return render_event_edit(request,conf_id,event,vars)
            
        return HttpResponseRedirect(BASEPATH+"/%s/events" % conf_id)
    else:
        return HttpResponseRedirect(BASEPATH+"/%s/events" % conf_id)


@admin_can_write
def event_delete(request, conf_id,event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    return HttpResponseRedirect(BASEPATH+"/%s/events" % conf_id)

