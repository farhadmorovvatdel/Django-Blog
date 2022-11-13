from django.contrib import messages
from django.shortcuts import redirect


def UserLoginRequired():
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            if  not request.user.is_authenticated:
                messages.error(request,'you must be log in','danger')
                return redirect('accounts:login')
            return view_func(request, *args, **kwargs)
        return wrap
    return decorator
