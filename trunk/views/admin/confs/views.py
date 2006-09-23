
from webcon.imports import *
from datetime import datetime
from psycopg import IntegrityError, ProgrammingError

MODULE = 'admin'
SUBMODULE = 'confs'
TPLPATH = MODULE+'/'+SUBMODULE
BASEPATH = '/'+MODULE+'/'+SUBMODULE


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
    archive_confs = ArchiveConference.objects.all().order_by('-end_date')
    vars = { 'basepath': BASEPATH }
    vars['confs'] = archive_confs
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
    hotels = [(h.id, h.name) for h in Hotel.objects.all().order_by('name')]

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
