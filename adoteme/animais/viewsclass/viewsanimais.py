from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView
from django.core.exceptions import ValidationError

from animais.services.baseanimaisservices import RacaService, TipoAnimalService
from animais.services.animaisservices import AnimalService
from principal.mixins import AbrigoMixin


class RacaListView(LoginRequiredMixin, ListView):
    template_name = "animais/racas/lista.html"
    context_object_name = "racas"

    def get_queryset(self):
        busca = self.request.GET.get("busca", "").strip()
        return RacaService().buscar_racas_por_nome(busca or None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["busca"] = self.request.GET.get("busca", "").strip()
        return context


class RacaCreateView(LoginRequiredMixin, AbrigoMixin, View):
    template_name = "animais/racas/form.html"

    def get(self, request, *args, **kwargs):
        tipos = TipoAnimalService().listar_tipos_animais()
        return render(request, self.template_name, {"tipos": tipos})

    def post(self, request, *args, **kwargs):
        nome = request.POST.get("nome", "").strip()
        tipo_animal_id = request.POST.get("tipo_animal_id")
        tipos = TipoAnimalService().listar_tipos_animais()
        try:
            RacaService().cadastrar_raca(nome, tipo_animal_id)
        except ValidationError as error:
            return render(request, self.template_name, {
                "erros": error.message_dict,
                "nome": nome,
                "tipo_animal_id": tipo_animal_id,
                "tipos": tipos,
            })
        messages.success(request, "Raça cadastrada com sucesso.")
        return redirect("animais:listar_racas")


class RacaUpdateView(LoginRequiredMixin, AbrigoMixin, View):
    template_name = "animais/racas/form.html"

    def get(self, request, raca_id):
        raca = RacaService().obter_raca_por_id(raca_id)
        if not raca:
            return redirect("animais:listar_racas")

        tipos = TipoAnimalService().listar_tipos_animais()
        return render(request, self.template_name, {
            "raca": raca,
            "nome": raca.nome,
            "tipo_animal_id": raca.tipo_animal_id,
            "tipos": tipos,
        })

    def post(self, request, raca_id):
        raca_service = RacaService()
        raca = raca_service.obter_raca_por_id(raca_id)
        if not raca:
            return redirect("animais:listar_racas")

        nome = request.POST.get("nome", "").strip()
        tipo_animal_id = request.POST.get("tipo_animal_id")
        tipos = TipoAnimalService().listar_tipos_animais()
        try:
            raca_service.atualizar_raca(raca_id, nome, tipo_animal_id)
        except ValidationError as error:
            return render(request, self.template_name, {
                "erros": error.message_dict,
                "raca": raca,
                "nome": nome,
                "tipo_animal_id": tipo_animal_id,
                "tipos": tipos,
            })
        messages.success(request, "Raça atualizada com sucesso.")
        return redirect("animais:listar_racas")


class RacaDeleteView(LoginRequiredMixin, AbrigoMixin, View):
    def post(self, request, raca_id):
        raca_service = RacaService()
        try:
            raca_service.excluir_raca(raca_id)
        except ValidationError:
            pass
        messages.success(request, "Raça excluída com sucesso.")
        return redirect("animais:listar_racas")


class AnimalCreateView(LoginRequiredMixin,AbrigoMixin, View):
    template_name = "animais/form.html"

    def get(self, request, *args, **kwargs):
        racas = RacaService().listar_racas()
        return render(request, self.template_name, {"racas": racas})

    def post(self, request, *args, **kwargs):
        AnimalService().cadastrar_animal(
            nome=request.POST.get("nome"),
            sexo=request.POST.get("sexo"),
            cor=request.POST.get("cor"),
            raca_id=request.POST.get("raca_id"),
            descricao=request.POST.get("descricao", ""),
            disponivel=request.POST.get("disponivel") == "on",
            dataNascimento=request.POST.get("dataNascimento"),
            foto=request.FILES.get("foto"),
        )
        messages.success(request, "Animal cadastrado com sucesso.")
        return redirect("animais:listar_animais")


class AnimalUpdateView(LoginRequiredMixin,AbrigoMixin, View):
    template_name = "animais/form.html"

    def get(self, request, animal_id):
        animal_service = AnimalService()
        animal = animal_service.obter_animal_por_id(animal_id)
        if not animal:
            return redirect("animais:listar_animais")

        racas = RacaService().listar_racas()
        return render(request, self.template_name, {"animal": animal, "racas": racas})

    def post(self, request, animal_id):
        animal_service = AnimalService()
        animal = animal_service.obter_animal_por_id(animal_id)
        if not animal:
            return redirect("animais:listar_animais")

        animal_service.atualizar_animal(
            animal_id=animal_id,
            nome=request.POST.get("nome"),
            sexo=request.POST.get("sexo"),
            cor=request.POST.get("cor"),
            raca_id=request.POST.get("raca_id"),
            descricao=request.POST.get("descricao", ""),
            disponivel=request.POST.get("disponivel") == "on",
            dataNascimento=request.POST.get("dataNascimento"),
            foto=request.FILES.get("foto"),
        )
        messages.success(request, "Animal atualizado com sucesso.")
        return redirect("animais:listar_animais")



class AnimalDeleteView(LoginRequiredMixin,AbrigoMixin, View):
    def post(self, request, animal_id):
        AnimalService().excluir_animal(animal_id)
        messages.success(request, "Animal excluído com sucesso.")
        return redirect("animais:listar_animais")


class AnimalListView(LoginRequiredMixin, ListView):
    template_name = "animais/lista.html"
    context_object_name = "animais"

    def get_queryset(self):
        busca = self.request.GET.get("busca", "").strip()
        return AnimalService().buscar(nome=busca or None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["busca"] = self.request.GET.get("busca", "").strip()
        return context