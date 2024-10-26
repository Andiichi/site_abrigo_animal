from django.contrib import admin

from cadastro_animal.models import CadastroAnimal
from .models import CadastroAdocao


@admin.action(description="Aprovar adoção selecionada e atualizar disponibilidade")
def aprovar_adocao(modeladmin, request, queryset):
    for adocao in queryset:
        adocao.aprovado = True
        adocao.save()
        animal = adocao.animal
        animal.disponivel = False
        animal.save()

class CadastroAdocaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'animal', 'aprovado')
    actions = [aprovar_adocao]