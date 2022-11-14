

from accounts.models import Profile
from django.shortcuts import Http404



class UpdateMixin:
    def dispatch(self,request,pk,*args, **kwargs):
        profile=Profile.objects.filter(id=pk).first()
        if  profile.user == request.user:
            return super(UpdateMixin,self).dispatch(request,*args,**kwargs)
        raise Http404('You dont have permission ')
