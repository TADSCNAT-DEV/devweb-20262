from django.contrib.auth.mixins import UserPassesTestMixin
from principal.utils import Utils

class AdotanteMixin(UserPassesTestMixin):
    raise_exception = True  # Levanta uma exceção se o teste falhar
    def test_func(self):
        if self.request.user.is_authenticated:
            tipo_usuario = Utils().verificar_tipo_usuario(self.request.user.id)
            return tipo_usuario == "ADOTANTE"
        return False

class AbrigoMixin(UserPassesTestMixin):
    raise_exception = True  # Levanta uma exceção se o teste falhar
    def test_func(self):
        if self.request.user.is_authenticated:
            tipo_usuario = Utils().verificar_tipo_usuario(self.request.user.id)
            return tipo_usuario == "ABRIGO"
        return False