from django.shortcuts import get_object_or_404, render

from .models import TipoAnimal,Raca,Animal

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

def listaranimais(request):
    nome=request.GET.get('nome','').strip()
    raca=request.GET.get('raca','').strip()
    racas=Raca.objects.all().order_by('nome')

    animais=Animal.objects.all().order_by('nome')

    if nome:
        animais=animais.objects.filter(nome__icontains=nome)
    if raca:
        animais=animais.objects.filter(raca=raca)
    
    return render(request,'animais/listanimais.html',{'animais':animais,'racas':racas,'raca':raca,'nome':nome})

