from django.shortcuts import get_object_or_404, render

from .models import TipoAnimal


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