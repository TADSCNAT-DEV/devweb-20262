from animais.models import Animal

class AnimalService:
    def obter_animal_por_id(self, animal_id):
        try:
            return Animal.objects.get(id=animal_id)
        except Animal.DoesNotExist:
            return None

    def listar_animais(self,disponivel=None):
        if disponivel is not None:
            return Animal.objects.filter(disponivel=disponivel)
        return Animal.objects.all()

    def buscar(self, nome=None, tipo_animal_id=None, raca_id=None, disponivel=None):
        queryset = Animal.objects.all() #pesquisa a alternativa com select related
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        if tipo_animal_id:
            queryset = queryset.filter(raca__tipo_animal_id=tipo_animal_id)
        if raca_id:
            queryset = queryset.filter(raca_id=raca_id)
        if disponivel is not None:
            queryset = queryset.filter(disponivel=disponivel)
        return queryset