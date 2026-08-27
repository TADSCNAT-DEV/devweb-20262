from django.urls import path
from . import views
urlpatterns = [
    path("/", views.index,name='index'),
    path("heloisa/",views.heloisa,name='heloisa'),
    path("tabuada2/",views.tabuada2,name='tabuada2'),
]