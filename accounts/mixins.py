from django.contrib import  messages
from django.shortcuts import redirect
from django.urls import  reverse_lazy



class AllowUserMixin:
    def dispatch(self,request,*args,**kwargs):
        user=[]
        if request.user.is_anonymous:
            user.append("is_anonymous")
        elif request.user.is_superuser:
            user.append("is_superuser")
        elif request.user.is_authenticated:
            user.append("is_authenticated")
        if user[0] not in self.allowed_user:
            messages.error(request, 'you should be  first login !', 'warning')
            return redirect(reverse_lazy('accounts:login'))
        else:
            return super().dispatch(request, *args, **kwargs)