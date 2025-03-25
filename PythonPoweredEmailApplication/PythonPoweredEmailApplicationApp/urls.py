from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# PythonPoweredEmailApplicationApp urls
urlpatterns = [
    path('', views.pythonPoweredEmailApplication, name='pythonpoweredemailapplication')
]