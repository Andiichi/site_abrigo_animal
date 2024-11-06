from django.contrib.auth import logout as django_logout, login as django_login
from django.contrib import messages, auth
from django.contrib.messages import constants
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

def cadastro_usuario(request):
    return render(request, 'templates_cadastrousuario/cadastro_usuario.html')

def lista_usuarios(request):
    return render(request, 'templates_cadastrousuario/lista_usuarios.html')


def login_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = auth.authenticate(username=nome, password=senha)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login realizado com sucesso.")
            return redirect('home')  # Redireciona para a página inicial ou para onde desejar
        else:
            messages.error(request, "Usuário ou senha inválidos.")
            return redirect('cadastro_usuario:login')  # Redireciona de volta para o login em caso de erro
    
    # Exibe a página de login ao invés de redirecionar em caso de GET
    return render(request, 'templates_cadastrousuario/login.html')


def logout_view(request):
    if request.method == "POST":
        django_logout(request)  # Chama o logout do Django
        messages.success(request, "Logout realizado com sucesso.")
        return redirect('home')  # Redireciona para a página inicial ou a que desejar
    return render(request, "templates_cadastrousuario/logout.html", {})
