
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import settings
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('blog/', include('blog.urls', namespace='blog'))
]
urlpatterns += [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
