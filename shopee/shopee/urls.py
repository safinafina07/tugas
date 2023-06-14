from django.contrib import admin
from django.urls import path
from beranda.views import beranda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('beranda/', beranda),
]
