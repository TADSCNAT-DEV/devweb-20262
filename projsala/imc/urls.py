from django.urls import path
from . import views

app_name = 'imc'

urlpatterns = [
    path("", views.index,name='index'),
    path("heloisa/",views.heloisa,name='heloisa'),
    path("tabuada2/",views.tabuada2,name='tabuada2'),
    path("calcular/",views.calcular_imc,name='calcular_imc')
]