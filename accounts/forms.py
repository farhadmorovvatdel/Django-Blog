from django import forms
from django.contrib.auth.models import User
from .models import Profile




# --------------  UserSignup Form ----------------
class SignupForms(forms.Form):
    username=forms.CharField(label='UserName',widget=forms.TextInput(attrs={'placeholder':'Please Enter Username','class':'form-control'}))
    last_name=forms.CharField(label='LastName',widget=forms.TextInput(attrs={'placeholder':'Please Enter LastName ','class':'form-control'}))
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder':'Please Enter Email','class':'form-control'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':'Please Enter Password','class':'form-control'}))
    password2=forms.CharField(label='ConfirmPassword',widget=forms.PasswordInput(attrs={'placeholder':'Please Enter ConfirmPassword','class':'form-control'}))

    def clean_username(self):
        username=self.cleaned_data['username']
        user=User.objects.filter(username=username).exists()
        if user:
            raise forms.ValidationError('this user already exists')
        return username
    def clean_password2(self):
        pass1=self.cleaned_data['password']
        pass2=self.cleaned_data['password2']
        if pass1 != pass2:
            raise forms.ValidationError('Passwords must be match')
        return pass1
    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise forms.ValidationError('this email already exists')
        return email


# --------------  UserLogin Form ----------------
class LoginForm(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'placeholder': 'Please enter Username','class': 'form-control'}))
    password = forms.CharField(label='Password ',
        widget=forms.PasswordInput(attrs={'placeholder': 'Please enter Password', 'class': 'form-control'}))

    def clean_firstname(self):
        username = self.cleaned_data['firstname']
        qs = User.objects.filter(username=username)
        if qs is None:
            raise forms.ValidationError('user with this information could not find')
        return qs


# --------------  EditProfile Form ----------------
class UpdateProfileForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(UpdateProfileForm, self).__init__(*args,**kwargs)
        self.fields['phone_number'].label='PhoneNumber'
        self.fields['image'].label='Set Profile Image'
    class Meta:
        model=Profile
        fields=('phone_number','image')
        widgets={
        'phone_number':forms.TextInput(attrs={'class':'form-control'}),
        'image':forms.FileInput(attrs={'class':'form-control'}),
      }


# --------------  UserChangePassword Form ----------------
class PasswordChangeForm(forms.Form):
    currentpassword = forms.CharField(label='UserPassword',
        widget=forms.PasswordInput(attrs={'placeholder': 'enter password', 'class': 'form-control'}))
    password = forms.CharField(label='New Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'enter password', 'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm New Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'enter confirm password', 'class': 'form-control'}))
    def clean_password2(self):
        pass1=self.cleaned_data['password']
        pass2=self.cleaned_data['password2']
        if pass1 and pass2 is None and pass1!= pass2:
            raise forms.ValidationError('passwords must be match')
        return pass2

class UserForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'placeholder': 'Please enter Username', 'class': 'form-control'}))


class UserForgotPasswordForm(forms.Form):
    password = forms.CharField(label='New Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'enter password', 'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm New Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'enter confirm password', 'class': 'form-control'}))
    def clean_password2(self):
        pass1=self.cleaned_data['password']
        pass2=self.cleaned_data['password2']
        if pass1 and pass2 is None and pass1 != pass2:
            raise forms.ValidationError('passwords must be match')
        return pass2