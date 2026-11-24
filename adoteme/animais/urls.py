from django.urls import path

from animais.viewsclass.viewstipoanimal import TipoAnimalListView,TipoAnimalCreateView,TipoAnimalUpdateView,TipoAnimalExcluirView
from animais.viewsclass.viewsanimais import (
    AnimalCreateView,
    AnimalDeleteView,
    AnimalListView,
    AnimalUpdateView,
    RacaCreateView,
    RacaDeleteView,
    RacaListView,
    RacaUpdateView,
)

app_name = 'animais'

urlpatterns = [
    path('tipos/', TipoAnimalListView.as_view(), name='listar_tipos_animais'),
    path('tipos/cadastrar/', TipoAnimalCreateView.as_view(), name='cadastrar_tipo_animal'),
    path('tipos/atualizar/<int:tipo_animal_id>/', TipoAnimalUpdateView.as_view(), name='atualizar_tipo_animal'),
    path('tipos/excluir/<int:tipo_animal_id>/', TipoAnimalExcluirView.as_view(), name='excluir_tipo_animal'),
    path('cadastrar/', AnimalCreateView.as_view(), name='cadastrar_animal'),
    path('atualizar/<int:animal_id>/', AnimalUpdateView.as_view(), name='atualizar_animal'),
    path('excluir/<int:animal_id>/', AnimalDeleteView.as_view(), name='excluir_animal'),
    path('racas/', RacaListView.as_view(), name='listar_racas'),
    path('racas/cadastrar/', RacaCreateView.as_view(), name='cadastrar_raca'),
    path('racas/atualizar/<int:raca_id>/', RacaUpdateView.as_view(), name='atualizar_raca'),
    path('racas/excluir/<int:raca_id>/', RacaDeleteView.as_view(), name='excluir_raca'),
    path('listar/', AnimalListView.as_view(), name='listar_animais'),
]
