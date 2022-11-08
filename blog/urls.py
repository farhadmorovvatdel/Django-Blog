from django.urls import path
from .views import All_Blogs,DetailPost,CreatePost,UserPost,DeletePost
app_name='blog'
urlpatterns=[
    path('',All_Blogs.as_view(),name='Blogs'),
    path('create/',CreatePost.as_view(),name='create_post'),
    path('userblog/',UserPost.as_view(),name='user_post'),
    path('delete/<int:pk>/',DeletePost.as_view(),name='delete_post'),
    path('<int:pk>/',DetailPost.as_view(),name='detail'),
]