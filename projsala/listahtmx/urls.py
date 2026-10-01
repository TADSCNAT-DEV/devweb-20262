from django.urls import path
from . import views

app_name = 'listahtmx'

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar/', views.buscar, name='buscar'),
]