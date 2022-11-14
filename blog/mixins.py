from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import Http404
from django.contrib import messages
from .models import Blog
from django.shortcuts import get_object_or_404,redirect


class UserLoginMixin:
    def dispatch(self, request,*args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request,'you must be logged in','danger')
            return redirect('accounts:login')
        return super(UserLoginMixin, self).dispatch(request,*args,**kwargs)


class UserAccessMixin:
    def dispatch(self,request,pk, *args, **kwargs):
        blog=get_object_or_404(Blog,pk=pk)
        if request.user == blog.user:
            return super(UserAccessMixin, self).dispatch(request,*args,**kwargs)
        else:
            raise Http404('you dont have permission')

