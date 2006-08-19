# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect

def login(request):
    # blabla
    return render_to_response('auth/auth_login.html')

def logout(request):
    # blabla
    return HttpResponseRedirect("/login")
