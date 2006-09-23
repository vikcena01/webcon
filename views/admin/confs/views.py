
from webcon.imports import *

MODULE = 'admin'
SUBMODULE = 'confs'
TPLPATH = MODULE+'/'+SUBMODULE
BASEPATH = '/'+MODULE+'/'+SUBMODULE

vars = { 'basepath': BASEPATH }

@admin_can_read
def index(request):
    actual_confs = ActualConference.objects.all().order_by('-start_date')
    comming_confs = CommingConference.objects.all().order_by('start_date')
    vars['actual_confs'] = actual_confs
    vars['comming_confs'] = comming_confs
    return render(TPLPATH+'/index.html', request, vars)


@admin_can_read
def archive(request):
    archive_confs = ArchiveConference.objects.all().order_by('-end_date')
    vars['confs'] = archive_confs
    return render(TPLPATH+'/archive.html', request, vars)

@admin_can_read
def overview(request, conf_id):
    conf = get_object_or_404(Conference, pk=conf_id)
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


@admin_can_write
def edit(request, conf_id=None):
    if conf_id:
        conf = get_object_or_404(Conference, pk=conf_id)
        contractors = [(c.id, c.name) for c in Contractor.objects.all().order_by('name')]
        hotels = [(h.id, h.name) for h in Hotel.objects.all().order_by('name')]

        vars['conf'] = conf
        vars['contractors'] = contractors
        vars['hotels'] = hotels
   
    return render(TPLPATH+'/edit.html', request, vars)
