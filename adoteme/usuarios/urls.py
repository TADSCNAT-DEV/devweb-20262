from django.urls import path

from usuarios.viewsclass.viewsusuarios import CadastroUsuarioView, LoginView, LogoutView

app_name='usuarios'

urlpatterns=[
    path('login/',LoginView.as_view(),name='login'),
    path('cadastro/',CadastroUsuarioView.as_view(),name='cadastro'),
    path('logout/',LogoutView.as_view(),name='logout'),
]