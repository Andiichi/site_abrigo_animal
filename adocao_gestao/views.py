from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from datetime import timezone

from .forms import FormCadastroAdocao
from .models import CadastroAdocao, RegrasAdocao


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
            return render(request, 'templates_gestaoadocao/adotar.html', contexto)
        else:
            contexto = {
                'form_adocao': form_adocao,
                'error': 'Error: Verifique as informações abaixo do formulário de adoção!'
            }
            return render(request, 'templates_gestaoadocao/adotar.html', contexto)
    
    else:
        form_adocao = FormCadastroAdocao()
        return render(request, 'templates_gestaoadocao/adotar.html', {'form_adocao': form_adocao})
 

def lista_adocoes(request):
    adocoes = CadastroAdocao.objects.all().order_by('nome')  # Ordena pelo nome do solicitante
    return render(request, 'templates_gestaoadocao/adocao_list.html', {'adocoes': adocoes})


def aprovar_desaprovar_adocao(request, adocao_id):
    # Obtém a solicitação de adoção ou retorna 404 se não encontrar
    adocao = get_object_or_404(CadastroAdocao, id=adocao_id)
    
    # Obtém a primeira regra de adoção associada
    regra_adocao = adocao.regras_adocoes.first()

    # import pdb; pdb.set_trace() #depurador python

    if regra_adocao:
        # Verifica se a solicitação está em um estado que pode ser aprovada
        if regra_adocao.solicitacao in ['feito', 'cancelado']:
            # Obtém o animal associado à adoção
            animal = adocao.animal
            # Altera o status de 'disponivel' para False
            animal.disponivel = False
            # Salva as mudanças no modelo CadastroAnimal
            animal.save()
            # Atualiza o status da regra para 'concluido'
            regra_adocao.solicitacao = 'concluido'
            regra_adocao.save()
            messages.success(request, "Adoção aprovada e animal marcado como indisponível.")

        elif regra_adocao.solicitacao == 'concluido':
            # Se o status já está 'concluido', muda para 'cancelado'
            animal = adocao.animal
            animal.disponivel = True
            animal.save()

            regra_adocao.solicitacao = 'cancelado'
            regra_adocao.save()

            messages.success(request, "Adoção cancelada e animal marcado como disponível.")
            
        else:
            messages.error(request, "Adoção não aprovada ou status inválido.")
    else:
        messages.error(request, "Nenhuma regra de adoção encontrada.")

    # Redireciona para a lista de adoções usando reverse
    return redirect(reverse('adocao_gestao:lista_adocoes'))
