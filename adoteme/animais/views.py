from django.shortcuts import get_object_or_404, render

from .models import TipoAnimal,Raca,Animal


def listatipoanimal(request):
    busca = request.GET.get('nome', '').strip()
    tipos = TipoAnimal.objects.all().order_by('nome')
    if busca:
        tipos = tipos.filter(nome__icontains=busca)
    return render(request, 'listatiposanimais.html', {'tipos': tipos, 'busca': busca})

def listaracas(request, tipo_id):
    tipo = get_object_or_404(TipoAnimal, pk=tipo_id)
    racas = tipo.racas.all().order_by('nome')
    return render(request, 'listaracas.html', {'tipo': tipo, 'racas': racas})

def listaranimais(request):
    nome=request.GET.get('nome','').strip()
    raca=request.GET.get('raca','').strip()
    racas=Raca.objects.all().order_by('nome')

    animais=Animal.objects.all().order_by('nome')

    if nome:
        animais=animais.objects.filter(nome__icontains=nome)
    if raca:
        animais=animais.objects.filter(raca=raca)
    
    return render(request,'listanimais.html',{'animais':animais,'racas':racas,'raca':raca,'nome':nome})