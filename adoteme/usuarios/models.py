from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.

class Usuario(User):
    nome=models.CharField(max_length=150,verbose_name="Nome do Usuário")
    cpf=models.CharField(max_length=11,verbose_name="CPF")
    tipo=models.CharField(max_length=10,choices=[("ADOTANTE","ADOTANTE"),("ABRIGO","ABRIGO")],verbose_name="Tipo do Usuário")

    def clean(self):
        erros={}
        if self.cpf and not self.cpf.isdigit():
            erros["cpf"].append("CPF deve conter apenas números.")
        if Usuario.objects.filter(cpf=self.cpf).exclude(pk=self.pk).exists():
            erros["cpf"].append("CPF já está em uso.")
        if Usuario.objects.filter(email=self.email).exclude(pk=self.pk).exists():
            erros["email"]="Email já está em uso."
        if Usuario.objects.filter(username=self.username).exclude(pk=self.pk).exists():
            erros["username"]="Nome de usuário já existe."
        if len(self.nome) < 3:
            erros["nome"]="O nome deve ter pelo menos 3 caracteres."
        if erros:
            raise ValidationError(erros)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name_plural="Usuários"
        verbose_name="Usuário"

class Perfil(models.Model):
    avatar=models.ImageField(upload_to="usuarios/avatar",verbose_name="Avatar do Usuário")
    comprovanteEnderecao=models.FileField(upload_to="usuarios/comprovantes",verbose_name="Comprovante de Endereço")
    bio=models.TextField(verbose_name="Biografia")
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE,verbose_name='Usuário')
    
    class Meta:
        verbose_name_plural="Perfis"
        verbose_name="Perfil"

    def __str__(self):
        return self.usuario.nome
