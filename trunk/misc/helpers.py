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
    'ch_conf_dates': 'Poda³e¶ niepoprawny termin konferencji!',
    'ch_conf_deadline': 'Termin rejestracji nie mo¿e przekraczaæ daty rozpoczêcia konferencji!',
    'ch_conf_cost': 'Cena konferencji nie mo¿e byæ ujemna!',
    'tg_activate_check_update':'Program konferencji jest pusty. Aktywacja wstrzymana',
    'tg_block_conf_update':'Konferencja trwa lub zakoñczyla siê. Aktualizacja danych niemo¿liwa',
    'ch_unique_admin': 'Admin o podanym loginie juz istnieje!',
}

def integrity_get_message(exc):
    for err in integrity_errors.keys():
        if err in exc:
            return integrity_errors[err]
    return 'Wyst±pi³ nieznany b³±d. Spróbuj ponownie.'+exc
    
    
    
    