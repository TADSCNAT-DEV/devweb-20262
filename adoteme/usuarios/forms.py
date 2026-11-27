from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from usuarios.models import Usuario


class CadastroUsuarioForm(forms.Form):
    nome = forms.CharField(label='Nome completo', max_length=150)
    username = forms.CharField(label='Usuário', max_length=150)
    email = forms.EmailField(label='E-mail')
    cpf = forms.CharField(label='CPF', max_length=11)
    password = forms.CharField(label='Senha', strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirme a senha', strip=False, widget=forms.PasswordInput)

    def clean(self):
        dados = super().clean()
        senha = dados.get('password')
        confirmacao = dados.get('password_confirm')
        if senha and confirmacao and senha != confirmacao:
            self.add_error('password_confirm', 'As senhas não conferem.')
        elif senha:
            # Validadores configurados em AUTH_PASSWORD_VALIDATORS
            usuario = Usuario(username=dados.get('username', ''), email=dados.get('email', ''))
            try:
                validate_password(senha, usuario)
            except ValidationError as e:
                self.add_error('password', e)
        return dados

    def adicionar_erros(self, erro):
        """Associa ao formulário os erros de um ValidationError lançado pelo service."""
        if not hasattr(erro, 'error_dict'):
            self.add_error(None, erro)
            return
        for campo, mensagens in erro.message_dict.items():
            self.add_error(campo if campo in self.fields else None, mensagens)
