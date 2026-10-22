from django.db import models

# Create your models here.

class Raridade(models.Model):
    nome=models.CharField(verbose_name="Raridade",max_length=100)
    descricao=models.TextField(verbose_name="Descrição")

    def __str__(self):
        return self.nome

class TipoPokemon(models.Model):
    nome=models.CharField(verbose_name="Tipo do Pokemon",max_length=100)

    def __str__(self):
        return self.nome

class CartaPokemon(models.Model):

    nome=models.CharField(verbose_name="Nome do Pokemon",max_length=100)
    estagioEvolucao=models.CharField(verbose_name="Estágio de Evolução",max_length=1,choices=[('1','COMUM'),('2','ESTÁGIO I'),('3','ESTÁGIO II')])
    pontoVida=models.IntegerField(verbose_name='Pontos de Vida',default=0)
    imagem=models.ImageField(verbose_name="Foto",upload_to='cartas/fotos')
    valorEstimado=models.DecimalField(verbose_name="Valor Estimado",decimal_places=2,max_digits=8)
    raridade=models.ForeignKey(Raridade,on_delete=models.PROTECT,related_name="pokemons")
    tipo=models.ForeignKey(TipoPokemon,on_delete=models.PROTECT,related_name="pokemons")

    def __str__(self):
        return self.nome
