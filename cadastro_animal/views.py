from django.shortcuts import render, get_object_or_404
import os
from django.utils import timezone
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import FormCadastroAnimal
from .models import GaleriaAnimal, CadastroAnimal

                     
def lista_animais(request):
    animais = CadastroAnimal.objects.filter(disponivel = True)
    
    return render(request, 'templates_home/home.html', {'animais': animais})

def cadastro(request):
    if request.method == 'POST':
        form_animal = FormCadastroAnimal(request.POST, request.FILES)
        animal_imagem = request.FILES.getlist('animal_imagem')

        if form_animal.is_valid():
            animal = form_animal.save(commit=False)  # Não salva ainda

           # Deixar os campos de nome e raça em minúsculo
            animal.nome = animal.nome.lower()
            animal.save()  # Salve o animal primeiro para gerar o ID

            # Salvar a data de criação
            data_criacao = timezone.now()
            data_formatada = data_criacao.strftime('%Y%m%d')  # Formato: YYYYMMDD

            # Criar o caminho da nova pasta
            nome_pasta = f"{animal.nome}"
            caminho_pasta = os.path.join(settings.MEDIA_ROOT, 'galeria', nome_pasta)
            os.makedirs(caminho_pasta, exist_ok=True)  # Cria a pasta se não existir


             # Salva as imagens
            for i, imagem in enumerate(animal_imagem):
                # Novo nome do arquivo com o nome do animal e data de criação (e índice para evitar conflito)
                novo_nome_arquivo = f"{animal.nome}_{data_formatada}_{i+1}.jpg"

                # Cria uma instância de FileSystemStorage para salvar no caminho da nova pasta
                fs = FileSystemStorage(location=caminho_pasta)

                # Salva a imagem no novo diretório com o nome ajustado
                caminho_imagem_salva = fs.save(novo_nome_arquivo, imagem)

                # Salva a referência da imagem no banco de dados
                GaleriaAnimal.objects.create(
                    animal=animal, 
                    imagem=os.path.join('galeria', nome_pasta, novo_nome_arquivo)
                )

            # Define sucesso como True
            contexto = {
                'form_animal': FormCadastroAnimal(),  # Reseta o formulário após o envio
                'sucesso': True
            }
            return render(request, 'templates_cadastroanimal/cadastro_animal.html', contexto)
        else:
            contexto = {
                'form_animal': form_animal,
                'error': 'Erro ao cadastrar animal. Verifique os dados informados.'
            }
            return render(request, 'templates_cadastroanimal/cadastro_animal.html', contexto)
    
    else:
        form_animal = FormCadastroAnimal()
        return render(request, 'templates_cadastroanimal/cadastro_animal.html', {'form_animal': form_animal})

                                        
def detalhe_animal(request, animal_id):
    # Busca o animal pelo ID, ou retorna 404 se não for encontrado
    animal = get_object_or_404(CadastroAnimal, id=animal_id)
    
    # Renderiza o template e passa o objeto `animal` como contexto
    return render(request, 'templates_cadastroanimal/detalhe_animal.html', {'animal': animal})

    
