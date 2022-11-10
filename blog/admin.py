from django.contrib import admin
from .models import Blog,Category,LikePost

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(LikePost)
