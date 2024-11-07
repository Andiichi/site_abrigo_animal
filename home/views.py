from django.shortcuts import render
from django.db.models import Q

from cadastro_animal.views import CadastroAnimal


def pesquisar_animais(request):
    if 'pesquisa_query' in request.GET:
        pesquisa_query = request.GET['pesquisa_query']

        #fazendo pessquisa com multiplas palavra chaves e campos
        query_clean = Q(Q(nome__icontains = pesquisa_query) | Q(especie__icontains = pesquisa_query))
        animais = CadastroAnimal.objects.filter(query_clean, disponivel = True)

        #fazendo pesquisa só de um campo
        # animais = CadastroAnimal.objects.filter(nome__icontains = pesquisa_query)
        
        return render(request, 'templates_home/pagina_pesquisa.html', {'pesquisa_query':pesquisa_query , 'animais': animais})
    
    else:
        return render(request, 'templates_home/pagina_pesquisa.html', {})