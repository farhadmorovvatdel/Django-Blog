from django.urls import path
from .views import All_Blogs,DetailPost,CreatePost,UserPost,DeletePost,AddComment,DeleteComment,\
    UpdateComment,AddLikePost
app_name='blog'
urlpatterns=[
    path('',All_Blogs.as_view(),name='Blogs'),
    path('create/',CreatePost.as_view(),name='create_post'),
    path('userblog/',UserPost.as_view(),name='user_post'),
    path('delete/<int:pk>/',DeletePost.as_view(),name='delete_post'),
    path('likepost/<int:post_id>/',AddLikePost,name='LikePost'),
    path('<int:pk>/',DetailPost.as_view(),name='detail'),
    path('addcomment/<int:id>/',AddComment,name='AddComment'),
    path('deletecomment/<int:comment_id>/',DeleteComment,name='DeleteComment'),
    path('updatecomment/<int:comment_id>/',UpdateComment,name='UpdateComment'),

]