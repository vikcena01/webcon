from django.http import HttpResponseRedirect,HttpResponse

def admin_logged(view_func):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    
    def _checklogin(request, *args, **kwargs):
        try:
            user_id = request.session['user_id']
            user_type = request.session['user_type']
            if user_id and user_type == 'admin':
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("Brak uprawnien do tej operacji!")
        except KeyError:
            return HttpResponseRedirect("/login")

    return _checklogin

def user_logged(view_func):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    
    def _checklogin(request, *args, **kwargs):
        try:
            user_id = request.session['user_id']
            user_type = request.session['user_type']
            if user_id and (user_type == 'admin' or user_type == 'normal'):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("Brak uprawnien do tej operacji!")
        except KeyError:
            return HttpResponseRedirect("/login")

    return _checklogin

