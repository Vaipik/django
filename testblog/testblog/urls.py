from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from myblog.views import page_not_found
from testblog import settings

urlpatterns = [
    path('', include('myblog.urls')),
    path('admin/', admin.site.urls, name='admin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found  # Typical name for 404
