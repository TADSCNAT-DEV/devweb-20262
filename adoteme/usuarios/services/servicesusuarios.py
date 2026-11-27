from usuarios.models import Usuario,Perfil
from django.core.exceptions import ValidationError
from django.db import transaction

class UsuarioService:
    @transaction.atomic
    def criar_usuario(self, username, email, password,cpf, nome, tipo):
        usuario = Usuario(username=username, email=email,cpf=cpf, nome=nome, tipo=tipo)
        usuario.set_password(password)
        try:
            usuario.full_clean()  # Valida o modelo antes de salvar
        except ValidationError as e:
            raise ValidationError(e.message_dict)
        usuario.save()
        perfil = Perfil(usuario=usuario)
        perfil.save()
        return usuario

    def atualizar_usuario(self, usuario_id, **kwargs):
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            for key, value in kwargs.items():
                setattr(usuario, key, value)
            try:
                usuario.full_clean()  # Valida o modelo antes de salvar
            except ValidationError as e:
                raise ValidationError(e.message_dict)
            usuario.save()
            return usuario
        except Usuario.DoesNotExist:
            raise ValidationError("Usuário não encontrado.")

    def deletar_usuario(self, usuario_id):
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            usuario.delete()
        except Usuario.DoesNotExist:
            raise ValidationError("Usuário não encontrado.")

    def listar_usuarios(self):
        return Usuario.objects.all()

    def consultar_tipo_usuario(self, usuario_id):
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            return usuario.tipo
        except Usuario.DoesNotExist:
            raise ValidationError("Usuário não encontrado.")

    def buscar_usuario_por_id(self, usuario_id):
        try:
            return Usuario.objects.get(id=usuario_id)
        except Usuario.DoesNotExist:
            raise ValidationError("Usuário não encontrado.")
    
    def atualizar_perfil(self, usuario_id, **kwargs):
        try:
            perfil = Perfil.objects.get(usuario__id=usuario_id)
            for key, value in kwargs.items():
                setattr(perfil, key, value)
            perfil.save()
            return perfil
        except Perfil.DoesNotExist:
            raise ValidationError("Perfil não encontrado.")