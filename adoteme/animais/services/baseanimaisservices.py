from animais.models import TipoAnimal, Raca
from django.core.exceptions import ValidationError, ObjectDoesNotExist, MultipleObjectsReturned

class TipoAnimalService:
    def obter_tipo_animal_por_id(self, tipo_animal_id):
        try:
            return TipoAnimal.objects.get(id=tipo_animal_id)
        except TipoAnimal.DoesNotExist:
            return None
        
    def listar_tipos_animais(self):
        return TipoAnimal.objects.all()
    
    def buscar_tipo_animal_por_nome(self, nome=None):
        if nome:
            return TipoAnimal.objects.filter(nome__icontains=nome)
        return TipoAnimal.objects.all()
    def cadastrar_tipo_animal(self,nome):
        tipo_animal = TipoAnimal(nome=nome)
        try:
            tipo_animal.full_clean()  # Valida o modelo antes de salvar
        except ValidationError as e:
            raise e  # Propaga a exceção para ser tratada em outro lugar
        tipo_animal.save()
        return tipo_animal
    def atualizar_tipo_animal(self, tipo_animal_id, nome):
        tipo_animal = self.obter_tipo_animal_por_id(tipo_animal_id)
        tipo_animal.nome = nome
        try:
            tipo_animal.full_clean()  # Valida o modelo antes de salvar
        except ValidationError as e:
            raise e  # Propaga a exceção para ser tratada em outro lugar
        tipo_animal.save()
        return tipo_animal

    def excluir_tipo_animal(self,tipo_animal_id):
        try:
            tipo_animal=TipoAnimal.objects.get(pk=tipo_animal_id)
            tipo_animal.delete()
        except ObjectDoesNotExist as e:
            raise ValidationError("Tipo de Animal não encontrado")

class RacaService:
    def obter_raca_por_id(self, raca_id):
        try:
            return Raca.objects.get(id=raca_id)
        except Raca.DoesNotExist:
            return None
    def listar_racas(self):
        return Raca.objects.all()
    def buscar_racas_por_nome(self, nome=None):
        if nome:
            return Raca.objects.filter(nome__icontains=nome)
        return Raca.objects.all()
    def buscar_racas_por_tipo(self, tipo_animal_id):
        return Raca.objects.filter(tipo_animal_id=tipo_animal_id)