from django.http import HttpResponseRedirect,HttpResponse

def admin_can_write(view_func):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    
    def _checklogin(request, *args, **kwargs):
        try:
            admin = request.session['admin']
            if admin and admin.can_write:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("Brak uprawnien do tej operacji!")
        except KeyError:
            return HttpResponseRedirect("/login")

    return _checklogin

def admin_can_read(view_func):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    
    def _checklogin(request, *args, **kwargs):
        try:
            admin = request.session['admin']
            # admin_type = request.session['admin_type']
            if admin:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("Brak uprawnien do tej operacji!")
        except KeyError:
            return HttpResponseRedirect("/login")

    return _checklogin
