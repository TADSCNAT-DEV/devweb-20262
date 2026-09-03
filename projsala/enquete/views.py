from django.shortcuts import render

# Create your views here.

def index(request):
    contexto = {
        'pergunta': 'Qual seu framework web favorito?',
        'alternativas': [
            {'id': 1, 'texto': 'Django'},
            {'id': 2, 'texto': 'Flask'},
            {'id': 3, 'texto': 'FastAPI'},
            {'id': 4, 'texto': 'Ruby on Rails'},
        ],
    }
    return render(request, 'enquete/index.html', context=contexto)
