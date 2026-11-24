from usuarios.services.servicesusuarios import UsuarioService
from django.core.exceptions import ValidationError
class Utils:
    def __init__(self):
        self.usuario_service = UsuarioService()

    def verificar_tipo_usuario(self, usuario_id):
        try:
            tipo_usuario = self.usuario_service.consultar_tipo_usuario(usuario_id)
            return tipo_usuario
        except ValidationError as e:
            return str(e)

def adoteme_context(request):
    context = {}
    if request.user.is_authenticated:
        context['USUARIO'] = request.user
    else:
        context['USUARIO'] = None
    tipo_usuario=Utils().verificar_tipo_usuario(request.user.id) if request.user.is_authenticated else None
    context['TIPO_USUARIO'] = tipo_usuario
    return context