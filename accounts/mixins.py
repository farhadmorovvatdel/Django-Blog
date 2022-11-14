from django.contrib import  messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import  reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User






class LoginUserMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'you must be login', 'danger')
            return redirect(reverse_lazy('accounts:login'))
        return super().dispatch(request, *args, **kwargs)



