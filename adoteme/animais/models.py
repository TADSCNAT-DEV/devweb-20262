from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class TipoAnimal(models.Model):
    nome = models.CharField(verbose_name="Nome",max_length=100,unique=True)

    def clean(self):
        erros={}
        if not self.nome:
            erros['nome']='O nome é obrigatório'
        elif len(self.nome)<3:
            erros['nome']='O nome precisa ter mais de 3 caracteres'
        if erros:
            raise ValidationError(erros)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Tipo de Animal"
        verbose_name_plural = "Tipos de Animais"
        ordering = ['nome']

class Raca(models.Model):
    nome = models.CharField(verbose_name="Nome",max_length=100)
    tipo_animal = models.ForeignKey(TipoAnimal,verbose_name="Tipo do Animal",on_delete=models.PROTECT,related_name='racas')

    def __str__(self):
        return f"{self.tipo_animal.nome}-{self.nome}"

    class Meta:
        verbose_name = "Raça"
        verbose_name_plural = "Raças"
        ordering = ['nome']
    
class Animal(models.Model):
    nome = models.CharField(verbose_name="Nome",max_length=255)
    sexo = models.CharField(verbose_name="Sexo",max_length=1,choices=[('M','Masculino'),('F','Feminino')])
    cor = models.CharField(verbose_name="Cor",max_length=50)
    raca = models.ForeignKey(Raca,verbose_name="Raça", on_delete=models.CASCADE,related_name='animais')
    descricao = models.TextField(verbose_name="Descrição", blank=True,null=True)
    disponivel = models.BooleanField(verbose_name="Disponível",default=True,null=True)
    dataNascimento=models.DateField(verbose_name="Data de Nascimento",help_text='Data não deve ser no futuro')
    foto=models.ImageField(upload_to="animais/fotos/",verbose_name="Foto do Animal",null=True)

    def __str__(self):
        return self.nome

    def idade(self):
        from datetime import date
        hoje = date.today()
        idade = hoje.year - self.dataNascimento.year - ((hoje.month, hoje.day) < (self.dataNascimento.month, self.dataNascimento.day))
        return idade

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"
        ordering = ['nome']


