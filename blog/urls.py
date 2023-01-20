from django.urls import path
from .views import All_Blogs,DetailPost,CreatePost,UserPost,DeletePost,UpdatePost,AddComment,DeleteComment,\
    UpdateComment,AddRate,AddLikePost,AddUnlikePost


app_name='blog'
urlpatterns=[
    path('',All_Blogs.as_view(),name='Blogs'),
    path('create/',CreatePost.as_view(),name='create_post'),
    path('userblog/',UserPost.as_view(),name='user_post'),
    path('delete/<int:pk>/',DeletePost.as_view(),name='delete_post'),
    path('update/<int:pk>/',UpdatePost.as_view(),name='update_post'),
    path('<int:pk>/',DetailPost.as_view(),name='detail'),
    path('addcomment/<int:id>/',AddComment,name='AddComment'),
    path('deletecomment/<int:comment_id>/',DeleteComment,name='DeleteComment'),
    path('updatecomment/<int:comment_id>/',UpdateComment,name='UpdateComment'),

    # path('unlikepost/<int:post_id>/', AddUnlikePost, name='UnLikePost'),
    # path('dislikepost/<int:post_id>/', AddDisLikePost, name='DisLikePost'),
    # path('disunlikepost/<int:post_id>/', AddUnDisLikePost, name='UnDisLikePost'),
    # path('likepost/<int:post_id>/',AddLikePost,name='LikePost'),
    path('addrate/<int:post_id>/',AddRate, name='AddRate'),
    path('likepost/<int:id>/',AddLikePost,name='LikePost'),
    path('unlikepost/<int:id>/',AddUnlikePost,name='UnLikePost')



]