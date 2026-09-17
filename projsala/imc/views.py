from django.shortcuts import render
from django.http import HttpResponse
from . import services
# Create your views here.

def index(request):
    return render(request,'index.html')
def heloisa(request):
    return HttpResponse("<h1>Olá Heloisa</h1>")
def tabuada2(request):
    n=2
    texto=''
    for numero in range(1,11):
        resultado=n*numero
        texto+=f'<h1>{n} x {numero}={resultado}</h1>'

    return HttpResponse(texto)

def calcular_imc(request):
    altura=float(request.POST["altura"])
    peso=float(request.POST["peso"])
    imc,classificacao=services.calcular_imc(altura,peso)
    contexto={
        'peso':peso,
        'altura':altura,
        'imc':f'{imc:.2f}',
        'classificacao':classificacao,
    }
    return render(request,'resultado.html',context=contexto)
