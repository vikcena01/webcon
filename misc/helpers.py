from django.template import RequestContext
from django.shortcuts import render_to_response
import re

def render(tplname, request, vars=None):
    return render_to_response(tplname, vars, context_instance=RequestContext(request))


def get_list_params(request, mod):
    
    page = int(request.GET.get('page', 0))
    
    if request.method == 'POST':
        page = 0
        keyword = request.POST.get('search_keyword', False)
        if keyword:
            request.session[mod+'_search_keyword'] = keyword
        else:
            request.session[mod+'_search_keyword'] = ""
    else:
        sort_by = request.GET.get('sort', False)
        sort_order = request.GET.get('order', 'asc')
        if sort_by:
            request.session[mod+'_sort_by'] = sort_by
            request.session[mod+'_sort_order'] = sort_order


    # pobieramy z sesji odpowiednie dane

    k = request.session.get(mod+'_search_keyword', "")
    if k:
        words = [w for w in re.split("\s+", k) if w] 
    else:
        words = []

    sort_by = request.session.get(mod+'_sort_by', "")
    sort_order = {'asc':'', 'desc':'-'}[request.session.get(mod+'_sort_order', "asc")]
    
    return (page, sort_by, sort_order, words)



integrity_errors = {
    'ch_conf_dates': 'Poda�e� niepoprawny termin konferencji!',
    'ch_conf_deadline': 'Termin rejestracji nie mo�e przekracza� daty rozpocz�cia konferencji!',
    'ch_conf_cost': 'Cena konferencji nie mo�e by� ujemna!',
    'tg_activate_check_update':'Program konferencji jest pusty. Aktywacja wstrzymana',
    'tg_block_conf_update':'Konferencja trwa lub zako�czyla si�. Aktualizacja danych niemo�liwa',
    'ch_unique_admin': 'Admin o podanym loginie juz istnieje!',
    'tg_block_conf_delete': 'Konferencja trwa. Usuni�cie niemo�liwe!',
    'event_time_insert': 'Niepoprawny czas dla wydarzenia!',
    'extra_time_insert': 'Niepoprawny czas dla opcji dodatkowej!',
}

def integrity_get_message(exc):
    for err in integrity_errors.keys():
        if err in exc:
            return integrity_errors[err]
    return 'Wyst�pi� nieznany b��d. Spr�buj ponownie.'+exc
    
    
    
    