from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

alternativas=[
            {'id': 1, 'texto': 'Django','votos':0},
            {'id': 2, 'texto': 'Flask','votos':0},
            {'id': 3, 'texto': 'FastAPI','votos':0},
            {'id': 4, 'texto': 'Ruby on Rails','votos':0},
        ]

def index(request):
    contexto = {
        'pergunta': 'Qual seu framework web favorito?',
        'alternativas': alternativas ,
    }
    return render(request, 'enquete/index.html', context=contexto)

def votar(request):
    opcao=int(request.GET["alternativa"])

    alternativa=alternativas[opcao-1]
    alternativa['votos']+=1

    contexto={'alternativas':alternativas}

    return render(request,'enquete/resultado.html',contexto)



