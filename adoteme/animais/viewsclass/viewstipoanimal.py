from django.views.generic import  ListView
from django.views import View
from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect
from animais.services.baseanimaisservices import TipoAnimalService
class TipoAnimalListView(ListView):
    template_name="animais/tipos/lista.html"
    context_object_name="tipos"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        busca=self.request.GET.get('busca','').strip()
        context['busca']=busca
        return context
    def get_queryset(self):
        busca=self.request.GET.get('busca','').strip()
        tipoAnimalService=TipoAnimalService()
        listaTipoAnimal=tipoAnimalService.buscar_tipo_animal_por_nome(busca)
        return listaTipoAnimal

class TipoAnimalCreateView(View):
    template_name="animais/tipos/form.html"
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)
    def post(self, request, *args, **kwargs):
        nome=request.POST.get("nome")
        tipoAnimalService=TipoAnimalService()
        try:
            tipoAnimalService.cadastrar_tipo_animal(nome)
        except ValidationError as e:
            return render(request,self.template_name,{'erros': e.message_dict, 'nome': nome})
        return redirect('animais:listar_tipos_animais')

class TipoAnimalUpdateView(View):
    template_name="animais/tipos/form.html"

    def get(self,request,tipo_animal_id):
        tipoAnimalService=TipoAnimalService()
        tipoAnimal=tipoAnimalService.obter_tipo_animal_por_id(tipo_animal_id)
        if not tipo_animal_id:
            return redirect('animais:listar_tipos_animais')
        return render(request,self.template_name,{'tipo_animal':tipoAnimal})

    def post(self,request,tipo_animal_id):
        tipoAnimalService=TipoAnimalService()
        tipoAnimal=tipoAnimalService.obter_tipo_animal_por_id(tipo_animal_id)
        nome = request.POST.get('nome')
        try:
            tipoAnimalService.atualizar_tipo_animal(tipo_animal_id, nome)
        except ValidationError as e:
            return render(request, self.template_name, {
                'erros': e.message_dict,
                'tipo_animal': tipoAnimal,
            })
        return redirect('animais:listar_tipos_animais')

class TipoAnimalExcluirView(View):
    def get(self,request,tipo_animal_id):
        tipoAnimalService=TipoAnimalService()
        tipoAnimal=tipoAnimalService.obter_tipo_animal_por_id(tipo_animal_id)
        try:
            tipoAnimalService.excluir_tipo_animal(tipo_animal_id)
        except ValidationError as e:
            return render(request, self.template_name, {
                            'erros': e.message_dict,
                            'tipo_animal': tipoAnimal,
                        })
        return redirect('animais:listar_tipos_animais')
