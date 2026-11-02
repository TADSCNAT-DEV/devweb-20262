from animais.models import TipoAnimal, Raca


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

class RacaService:
    def obter_raca_por_id(self, raca_id):
        try:
            return Raca.objects.get(id=raca_id)
        except Raca.DoesNotExist:
            return None
    def listar_racas(self):
        return Raca.objects.all()
    def buscar_racar_por_nome(self, nome):
        return Raca.objects.filter(nome__icontains=nome)
    def listar_racas_por_tipo(self, tipo_animal_id):
        return Raca.objects.filter(tipo_animal_id=tipo_animal_id)