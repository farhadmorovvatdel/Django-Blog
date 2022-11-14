from django.contrib import admin
from .models import Blog,Category,RatePost,Comment

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(RatePost)
admin.site.register(Comment)

