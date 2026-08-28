from django.shortcuts import render
from django.http import HttpResponse

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

def calcular_imc(request,altura,peso):
    altura=altura/100.0
    resposta=f'O Valor do IMC é {(peso/(altura*altura)):.2f}'
    return HttpResponse(resposta)
