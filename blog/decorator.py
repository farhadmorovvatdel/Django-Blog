from django.contrib import messages
from django.shortcuts import redirect
from .models import Comment
from django.shortcuts import get_object_or_404,Http404

def UserLoginRequired():
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            if  not request.user.is_authenticated:
                messages.error(request,'you must be log in','danger')
                return redirect('accounts:login')
            return view_func(request, *args, **kwargs)
        return wrap
    return decorator



def UserAccess():
    def decorator(view_func):
        def wrap(request,comment_id,*args, **kwargs):
                comment=get_object_or_404(Comment,pk=comment_id)
                if request.user == comment.user:
                    return view_func(request,comment_id,*args, **kwargs)
                raise Http404('you dont have permission')
        return wrap
    return decorator
