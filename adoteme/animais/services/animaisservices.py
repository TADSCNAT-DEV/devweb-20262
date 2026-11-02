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

    def cadastrar_animal(self, nome, sexo, cor, raca_id, descricao, disponivel, dataNascimento, foto):
        animal = Animal(
            nome=nome,
            sexo=sexo,
            cor=cor,
            raca_id=raca_id,
            descricao=descricao,
            disponivel=disponivel,
            dataNascimento=dataNascimento,
            foto=foto
        )
        animal.save()
        return animal

    def atualizar_animal(self, animal_id, **kwargs):
        campos_atualizaveis = {
            "nome",
            "sexo",
            "cor",
            "raca_id",
            "descricao",
            "disponivel",
            "dataNascimento",
            "foto",
        }
        campos_opcionais = {"descricao", "disponivel"}

        campos_invalidos = kwargs.keys() - campos_atualizaveis
        if campos_invalidos:
            campo = next(iter(campos_invalidos))
            raise TypeError(f"atualizar_animal() got an unexpected keyword argument '{campo}'")

        animal = self.obter_animal_por_id(animal_id)
        if animal:
            for campo, valor in kwargs.items():
                if (campo in campos_opcionais and valor is not None) or (
                    campo not in campos_opcionais and valor
                ):
                    setattr(animal, campo, valor)
            animal.save()
        return animal

    def excluir_animal(self, animal_id):
        animal = self.obter_animal_por_id(animal_id)
        if animal:
            animal.delete()
            return True
        return False