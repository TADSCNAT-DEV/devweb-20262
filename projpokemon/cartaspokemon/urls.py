from django.urls import path
from . import views

app_name = 'cartaspokemon'

urlpatterns = [
    path('', views.index, name='index'),
    path('cartas/<int:raridade_id>/', views.lista_carta_raridade, name='lista_carta_raridade'),
]
