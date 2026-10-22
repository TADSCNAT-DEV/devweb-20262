from django.shortcuts import render
from .models import Raridade,CartaPokemon
# Create your views here.

def index(request):
    raridades=Raridade.objects.all()
    lista_raridades=[]
    for raridade in raridades:
        if raridade.pokemons.count()>0:
            lista_raridades.append(raridade)
    return render(request,"index.html",{'raridades':lista_raridades})

def lista_carta_raridade(request,raridade_id):
    cartas=CartaPokemon.objects.filter(raridade=raridade_id)
    busca=request.GET.get('nome')
    if busca and cartas:
        cartas=cartas.filter(nome__icontains=busca)
    return render(request,'cartas.html',{'cartas':cartas,'busca':busca})
        
