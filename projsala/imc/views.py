from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
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

def mensagem(request):

    if (request.htmx):
        mensagem='Olá HTMX!!!'
        contexto={
            'mensagem':mensagem
        }
        return render(request,"mensagem.html",contexto)
    else:    
        dicionario={'mensagem':'Olá IMC - Dev Web'}
        return JsonResponse(dicionario)

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
    if request.htmx:
        return render(request,'resultado_partial.html',context=contexto)
    else:
        return render(request,'resultado.html',context=contexto)
