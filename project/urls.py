from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),#needed for django built in password reset etc
    path('', include('managementportal.urls')),
    path('', include('staffportal.urls')),
    path('', include('studentportal.urls')),
    path('', include('core.urls')),
    path('', include('applications.urls')),
    path('', include('aspirantportal.urls')),


]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.STATIC_ROOT)

