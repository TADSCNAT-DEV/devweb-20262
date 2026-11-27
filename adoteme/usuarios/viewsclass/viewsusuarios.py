from django.views import View
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.exceptions import ValidationError

from usuarios.forms import CadastroUsuarioForm
from usuarios.services.servicesusuarios import UsuarioService

class LoginView(View):
    template_name='usuarios/login.html'
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('principal:index_logado')
        return render(request,self.template_name)
    def post(self,request):
        if request.user.is_authenticated:
            return redirect('principal:index_logado')
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('principal:index_logado')
        else:
            return render(request,self.template_name,{'error':'Usuário ou senha inválidos'})
class LogoutView(View):
    def get(self,request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('principal:index')
        

class CadastroUsuarioView(View):
    template_name = 'usuarios/cadastro.html'
    form_class = CadastroUsuarioForm

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = UsuarioService()

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('principal:index_logado')
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('principal:index_logado')

        form = self.form_class(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            try:
                self.service.criar_usuario(
                    username=dados['username'],
                    email=dados['email'],
                    password=dados['password'],
                    cpf=dados['cpf'],
                    nome=dados['nome'],
                    tipo="ADOTANTE"
                )
            except ValidationError as e:
                form.adicionar_erros(e)
            else:
                messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
                return redirect('usuarios:login')

        return render(request, self.template_name, {'form': form})
