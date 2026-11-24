from django.contrib import admin
from django.urls import path
from Composta.views import inicio, pasos, tipos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('pasos/', pasos, name='pasos'),
    path('tipos/', tipos, name='tipos'),
]