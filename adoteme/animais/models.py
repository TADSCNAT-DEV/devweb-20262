from django.db import models

# Create your models here.

class TipoAnimal(models.Model):
    nome = models.CharField(max_length=100)

class Raca(models.Model):
    nome = models.CharField(max_length=100)
    tipo_animal = models.ForeignKey(TipoAnimal,on_delete=models.PROTECT,related_name='racas')

class Animal(models.Model):
    nome = models.CharField(max_length=255)
    sexo = models.CharField(max_length=1,choices=[('M','Masculino'),('F','Feminino')])
    cor = models.CharField(max_length=50)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE,related_name='animais')
    descricao = models.TextField(blank=True,null=True)
    disponivel = models.BooleanField(default=True,null=True)
    dataNascimento=models.DateField()


