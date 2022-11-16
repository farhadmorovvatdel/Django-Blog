from django.urls import path
from .views import Register,LoginView,UserLogOut,UserProfile,UpdateProfile,PasswordChange


app_name='accounts'
urlpatterns=[
    path('register',Register.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout',UserLogOut,name='logout'),
    path('profile/',UserProfile.as_view(),name='profile'),
    path('profile/<int:pk>/',UpdateProfile.as_view(),name='upateprofile'),
    path('passwordchange/',PasswordChange.as_view(),name='passwordchange'),

]
