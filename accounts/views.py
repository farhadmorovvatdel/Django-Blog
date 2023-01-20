from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import UpdateView

from .forms import SignupForms,LoginForm,UserForm,UserForgotPasswordForm

from  django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib import messages
from .models import Profile
from .forms import UpdateProfileForm
from .mixins import UpdateMixin
from.forms import PasswordChangeForm
from django.contrib.auth import authenticate
from blog.mixins import UserLoginMixin

class Register(View):

    """
     Register User
    """

    form_class=SignupForms
    def get(self,request):
        form=self.form_class
        return render(request,'accounts/register.html',{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            last_name=form.cleaned_data.get('last_name')
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            user=User.objects.create_user(username=username,last_name=last_name,email=email,password=password)
            user.save()
            messages.success(request,'you register','success')
            return  redirect('accounts:login')
        return render(request,'accounts/register.html',{'form':form})


class LoginView(View):
    """
     Login User
    """
    form_class = LoginForm
    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/login.html', {'form': form})
    def post(self, request):
        form = LoginForm(request.POST,request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user:
             login(request,user)
             messages.success(request,'You Logged in your account','success')
             return redirect('accounts:profile')

            else:
                messages.error(request,'User or Password is incorrect ','danger')
                return redirect('accounts:login')

        return render(request, 'accounts/login.html', {'form': form})




def UserLogOut(request):
    """
     Logout User
    """
    logout(request)
    return  redirect('accounts:login')



class UserProfile(View):
    """
     User Profile
    """

    def get(self,request):
        profile=Profile.objects.get(user_id=request.user.id)
        return render(request,'accounts/profile.html',{'profile':profile})

class UpdateProfile(UserLoginMixin,UpdateMixin,UpdateView):
    """
     Update Profile User
    """

    template_name = 'accounts/updateprofile.html'
    form_class = UpdateProfileForm
    model = Profile

    def get_context_data(self, **kwargs):
       id=self.kwargs['pk']
       context= super(UpdateProfile, self).get_context_data()
       context['profile']=Profile.objects.filter(id=id).only('image').first()
       return  context



    def get_success_url(self):
        return  reverse_lazy('accounts:profile')











class PasswordChange(UserLoginMixin,View):
    """
     Change Password User
    """
    def get(self,request):
        profile=request.user.profile
        form = PasswordChangeForm()
        return render(request, 'accounts/PasswordChange.html', {'form':form,'profile':profile})

    def post(self,request):
        form=PasswordChangeForm(request.POST)
        if form.is_valid():
            current_password=form.cleaned_data['currentpassword']
            pass1=form.cleaned_data['password']
            pass2=form.cleaned_data['password2']
            user=User.objects.filter(username=request.user.username).first()
            if user.check_password(current_password) and pass1 == pass2:
                user.set_password(pass1)
                user.save()
                logout(request)
                return redirect(reverse_lazy('accounts:login'))
            elif pass1 != pass2:
                form.add_error('password','Passwords must be match')
            else:
                form.add_error('currentpassword','Password is wrong')
        return render(request, 'accounts/PasswordChange.html', {'form': form})

class UserView(View):
    def get(self, request):
        form=UserForm()
        return render(request, 'accounts/user.html',{'form': form})
    def post(self,request):
        form=UserForm(request.POST)
        global user
        if form.is_valid():
            username=form.cleaned_data['username']
            user=User.objects.filter(username=username).first()
            if user :
               return redirect("accounts:userforgotpasswordview",user.username)

        else:
            form.add_error('username',"username is uncorrect")

        return render(request, 'accounts/user.html', {'form':form,"user":user})


class UserForgotPasswordView(View):
    def get(self, request,*args, **kwargs):
        name=kwargs["name"]

        form =UserForgotPasswordForm()

        return render(request, 'accounts/userforgotpasswordform.html',{"form":form})
    def post(self,request,*args,**kwargs):
        name=kwargs["name"]
        form=UserForgotPasswordForm(request.POST)
        if form.is_valid():
            pass1=form.cleaned_data['password']
            user=User.objects.filter(username=name).first()
            if user:
                user.set_password(pass1)
                user.save()
                return redirect("accounts:login")

        return render(request, 'accounts/userforgotpasswordform.html', {"form": form})


