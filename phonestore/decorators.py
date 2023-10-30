from django.shortcuts import redirect
from django.contrib import messages

#create our decorator
def notLoggedUsers(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, 'Ops! User  already loged!')
            return redirect('dashboard')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowedusers(allowedGroups=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group= None
            if request.user.groups.exists():
                group= request.user.groups.all()[0].name
                if group in allowedGroups:
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect ('profile')
            return wrapper_func
    return decorator

