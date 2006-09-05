from django.http import HttpResponseRedirect

def admin_logged(view_func):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    
    def _checklogin(request, *args, **kwargs):
        try:
            user_id = request.session['user_id']
            # user_role = request.session['user_role']
            if user_id:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseRedirect("/login")
        except KeyError:
            return HttpResponseRedirect("/login")

    return _checklogin

