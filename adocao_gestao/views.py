from django.shortcuts import render,get_object_or_404, redirect
from datetime import timezone

from .models import CadastroAdocao
from .forms import FormCadastroAdocao


def cadastro_adocao(request):
    if request.method == 'POST':
        form_adocao = FormCadastroAdocao(request.POST)

        if form_adocao.is_valid():
            # Salva a adoção
            form_adocao.save()
            # Redefine o formulário após o envio
            contexto = {
                'form_adocao': FormCadastroAdocao(),  # Reseta o formulário após o envio
                'sucesso': True
            }
            return render(request, 'adotar.html', contexto)
        else:
            contexto = {
                'form_adocao': form_adocao,
                'error': 'Error: Verifique as informações abaixo do formulário de adoção!'
            }
            return render(request, 'adotar.html', contexto)
    
    else:
        form_adocao = FormCadastroAdocao()
        return render(request, 'adotar.html', {'form_adocao': form_adocao})
 