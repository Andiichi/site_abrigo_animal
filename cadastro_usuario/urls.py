from django.urls import path

from . import views

app_name = 'cadastro_usuario'

urlpatterns = [
    path("cadastro-usuario/", views.cadastro_usuario, name="cadastro_usuario"),
    path('lista-usuarios/', views.lista_usuarios, name='lista_usuarios'),
]