from django.shortcuts import render
from animais.services.animaisservices import AnimalService
from animais.services.baseanimaisservices import RacaService, TipoAnimalService

animaiservice = AnimalService()
raca_service = RacaService()
tipo_animal_service = TipoAnimalService()


def index_logado(request):
    context = {
        'total_animais':animaiservice.listar_animais().count(),
        'total_racas': raca_service.listar_racas().count(),
        'total_pedidos_adocao': 0,
        'pedidos_em_analise': 0,
        'animais_disponiveis': animaiservice.listar_animais(disponivel=True).count(),
        'animais_indisponiveis': animaiservice.listar_animais(disponivel=False).count(),
    }
    return render(request, 'principal/interna/index.html', context)

def index_publico(request):
    nome = request.GET.get('nome', '').strip()
    tipo = request.GET.get('tipo', '').strip()
    raca = request.GET.get('raca', '').strip()
    disponibilidade = request.GET.get('disponivel', 'todos').strip() or 'todos'

    disponivel = None
    if disponibilidade == 'sim':
        disponivel = True
    elif disponibilidade == 'nao':
        disponivel = False

    animais = animaiservice.buscar(
        nome=nome or None,
        tipo_animal_id=tipo or None,
        raca_id=raca or None,
        disponivel=disponivel,
    )

    context = {
        'animais': animais,
        'animais_disponiveis': animaiservice.listar_animais(disponivel=True),
        'tipos': tipo_animal_service.listar_tipos_animais(),
        'racas': raca_service.listar_racas(),
        'filtro_nome': nome,
        'filtro_tipo': tipo,
        'filtro_raca': raca,
        'filtro_disponivel': disponibilidade,
        'total_animais': animaiservice.listar_animais().count(),
        'total_tipos': tipo_animal_service.listar_tipos_animais().count(),
        'total_adocoes': 0,
    }
    return render(request, 'principal/landing/index.html', context)

