from django.urls import path

from . import views

app_name = 'cadastro_usuario'

urlpatterns = [
    path("registro/", views.cadastro_usuario, name="cadastro_usuario"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('lista-usuarios/', views.lista_usuarios, name='lista_usuarios'),
]