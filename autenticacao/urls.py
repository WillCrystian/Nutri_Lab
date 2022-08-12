from django.urls import path
from . import views

urlpatterns = [
    #nome a ser mostrado na url/ nome da função/ nome de acesso
    path('cadastro/', views.cadastro, name="cadastro"),
    path('logar/', views.logar, name="logar"),
    path('sair/', views.sair, name="sair"),
    path('ativar_conta/<str:token>/', views.ativar_conta, name= "ativar_conta")


]