from django.urls import path

from . import views

from animais.viewsclass.viewstipoanimal import TipoAnimalListView,TipoAnimalCreateView,TipoAnimalUpdateView,TipoAnimalExcluirView

app_name = 'animais'

urlpatterns = [
    path('tipos/', TipoAnimalListView.as_view(), name='listar_tipos_animais'),
    path('tipos/cadastrar/', TipoAnimalCreateView.as_view(), name='cadastrar_tipo_animal'),
    path('tipos/atualizar/<int:tipo_animal_id>/', TipoAnimalUpdateView.as_view(), name='atualizar_tipo_animal'),
    path('tipos/excluir/<int:tipo_animal_id>/', TipoAnimalExcluirView.as_view(), name='excluir_tipo_animal'),
    path('cadastrar/', views.cadastrar_animal, name='cadastrar_animal'),
    path('atualizar/<int:animal_id>/', views.atualizar_animal, name='atualizar_animal'),
    path('excluir/<int:animal_id>/', views.excluir_animal, name='excluir_animal'),
    path('racas/',views.listar_racas,name='listar_racas'),
    path('listar/', views.listaranimais, name='listar_animais'),
]
