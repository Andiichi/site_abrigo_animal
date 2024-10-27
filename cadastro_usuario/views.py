from django.shortcuts import render

# Create your views here.

def cadastro_usuario(request):
    return render(request,'cadastro_usuario.html')

def lista_usuarios(request):
    return render(request,'lista_usuarios.html')