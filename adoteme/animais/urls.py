from django.urls import path

from . import views

app_name = 'animais'

urlpatterns = [
    path('tipos/', views.listar_tipos_animais, name='listar_tipos_animais'),
    path('cadastrar/', views.cadastrar_animal, name='cadastrar_animal'),
    path('atualizar/<int:animal_id>/', views.atualizar_animal, name='atualizar_animal'),
    path('excluir/<int:animal_id>/', views.excluir_animal, name='excluir_animal'),
    path('listar/', views.listaranimais, name='listar_animais'),
    path('tipos_old/', views.listatipoanimal, name='listatipoanimal'),
    path('tipos_old/<int:tipo_id>/racas/', views.listaracas, name='listaracas'),
]
