from django.shortcuts import render
# Create your views here.
alunos = [
        {'nome': 'Ana', 'curso': 'ADS'},
        {'nome': 'João', 'curso': 'SI'},
        {"nome": "Ana Lima",
         "curso": "Computação"},
        {"nome": "Bruno Costa",
         "curso": "Engenharia"},
        {"nome": "Carla Souza",
         "curso": "Sistemas"},
    ]
def index(request):
    return render(request,'listahtmx/index.html',{'alunos': alunos})
def buscar(request):
    q = request.GET.get('q', '')
    if q:
        alunos_consulta = [a for a in alunos if q.lower() in a['nome'].lower() or q.lower() in a['curso'].lower()]
    else:
        alunos_consulta = alunos
    return render(request, 'listahtmx/lista.html', {'alunos': alunos_consulta, 'q': q})