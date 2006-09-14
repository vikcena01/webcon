from django.template import RequestContext
from django.shortcuts import render_to_response

def render(tplname, request, vars=None):
    return render_to_response(tplname, vars, context_instance=RequestContext(request))
