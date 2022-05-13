# mysite/urls.py
from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('yoway/', include('server.urls')),
    path('admin/', admin.site.urls),
]