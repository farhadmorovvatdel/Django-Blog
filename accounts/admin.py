from django.contrib import admin
from .models import Profile


# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['user', 'phone_number']
#     list_filter = ['user']
#     list_editable = ['phone_number']

admin.site.register(Profile)