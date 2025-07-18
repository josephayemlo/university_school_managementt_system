from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('management/', include('managementportal.urls')),
    path('staff/', include('staffportal.urls')),
    path('studentportal/', include('studentportal.urls')),
    path('', include('core.urls')),
    path('applications/', include('applications.urls')),
    path('aspirantportal/', include('aspirantportal.urls')),
    path('studentchat/', include('studentchat.urls')),



]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.STATIC_ROOT)

