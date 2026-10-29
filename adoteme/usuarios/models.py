from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(User):
    nome=models.CharField(max_length=150,verbose_name="Nome do Usuário")
    cpf=models.CharField(max_length=11,verbose_name="CPF")
    tipo=models.CharField(max_length=10,choices=[("ADOTANTE","ADOTANTE"),("ABRIGO","ABRIGO")],verbose_name="Tipo do Usuário")

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

    def __str__(self):
        return self.usuario.nome
