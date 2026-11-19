from django.views import View
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render,redirect

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
        