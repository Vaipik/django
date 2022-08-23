from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from myblog.views import pageNotFound
from testblog import settings

urlpatterns = [
    path('', include('myblog.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound  # Typical name for 404