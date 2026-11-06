from django.shortcuts import get_object_or_404, render,redirect

from .models import TipoAnimal,Raca,Animal
from django.core.exceptions import ValidationError
from .services.baseanimaisservices import TipoAnimalService, RacaService
from .services.animaisservices import AnimalService

tipo_animal_service = TipoAnimalService()
raca_service = RacaService()
animal_service = AnimalService()

def listatipoanimal(request):
    busca = request.GET.get('nome', '').strip()
    tipos = tipo_animal_service.buscar_tipo_animal_por_nome(busca)
    return render(request, 'animais/listatiposanimais.html', {'tipos': tipos, 'busca': busca})

def listaracas(request, tipo_id):
    tipo = tipo_animal_service.obter_tipo_animal_por_id(tipo_id)
    racas = raca_service.listar_racas_por_tipo(tipo_id)
    return render(request, 'animais/listaracas.html', {'tipo': tipo, 'racas': racas})

#Implementaação valendo são as views a seguir, as views acima são antigas e não estão sendo usadas no projeto, mas não foram deletadas para não quebrar o código do projeto.

def listar_tipos_animais(request):
    busca=request.GET.get('busca', '').strip()
    tipos = tipo_animal_service.buscar_tipo_animal_por_nome(busca or None)
    return render(request, 'animais/tipos/lista.html', {'tipos': tipos,'busca':busca})

def cadastrar_tipo_animal(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        try:
            tipo_animal_service.cadastrar_tipo_animal(nome)
        except ValidationError as e:
            return render(request, 'animais/tipos/form.html', {'erros': e.message_dict, 'nome': nome})
        return redirect('animais:listar_tipos_animais')
    return render(request, 'animais/tipos/form.html')


def atualizar_tipo_animal(request, tipo_animal_id):
    tipo_animal = tipo_animal_service.obter_tipo_animal_por_id(tipo_animal_id)
    if not tipo_animal:
        return redirect('animais:listar_tipos_animais')
    if request.method == 'POST':
        nome = request.POST.get('nome')
        try:
            tipo_animal_service.atualizar_tipo_animal(tipo_animal_id, nome)
        except ValidationError as e:
            return render(request, 'animais/tipos/form.html', {
                'erros': e.message_dict,
                'tipo_animal': tipo_animal,
                'nome': nome,
            })
        return redirect('animais:listar_tipos_animais')

    return render(request, 'animais/tipos/form.html', {
        'tipo_animal': tipo_animal,
        'nome': tipo_animal.nome,
    })

def excluir_tipo_animal(request, tipo_animal_id):
    tipo_animal = tipo_animal_service.obter_tipo_animal_por_id(tipo_animal_id)
    if tipo_animal:
        tipo_animal.delete()
    return redirect('animais:listar_tipos_animais')

def listar_racas(request):
    busca=request.GET.get('busca','').strip()
    racas=raca_service.buscar_racas_por_nome(busca or None)
    return render(request,'animais/racas/lista.html',{'racas':racas,'busca':busca})


def cadastrar_animal(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sexo = request.POST.get('sexo')
        cor = request.POST.get('cor')
        raca_id = request.POST.get('raca_id')
        descricao = request.POST.get('descricao', '')
        disponivel = request.POST.get('disponivel') == 'on'
        dataNascimento = request.POST.get('dataNascimento')
        foto = request.FILES.get('foto')

        animal_service.cadastrar_animal(
            nome=nome,
            sexo=sexo,
            cor=cor,
            raca_id=raca_id,
            descricao=descricao,
            disponivel=disponivel,
            dataNascimento=dataNascimento,
            foto=foto
        )
        return redirect('animais:listar_animais')
    racas = raca_service.listar_racas()
    return render(request, 'animais/form.html', {'racas': racas})

def atualizar_animal(request, animal_id):
    animal = animal_service.obter_animal_por_id(animal_id)
    if not animal:
        return redirect('animais:listar_animais')

    if request.method == 'POST':
        nome = request.POST.get('nome')
        sexo = request.POST.get('sexo')
        cor = request.POST.get('cor')
        raca_id = request.POST.get('raca_id')
        descricao = request.POST.get('descricao', '')
        disponivel = request.POST.get('disponivel') == 'on'
        dataNascimento = request.POST.get('dataNascimento')
        foto = request.FILES.get('foto')

        animal_service.atualizar_animal(
            animal_id=animal_id,
            nome=nome,
            sexo=sexo,
            cor=cor,
            raca_id=raca_id,
            descricao=descricao,
            disponivel=disponivel,
            dataNascimento=dataNascimento,
            foto=foto
        )
        return redirect('animais:listar_animais')

    racas = raca_service.listar_racas()
    return render(request, 'animais/form.html', {'animal': animal, 'racas': racas})

def excluir_animal(request, animal_id):
    animal = animal_service.obter_animal_por_id(animal_id)
    if animal:
        animal_service.excluir_animal(animal_id)
    return redirect('animais:listar_animais')

def listaranimais(request):
    busca=request.GET.get('busca', '').strip()
    animais=animal_service.buscar(nome=busca or None)
    return render(request,'animais/lista.html',{'animais':animais,'busca':busca})

