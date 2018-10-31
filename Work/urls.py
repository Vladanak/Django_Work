from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
from Work import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('app.urls')),
    url(r'schedule/',include('schedule.urls'))
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
