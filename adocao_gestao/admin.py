from django.contrib import admin
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.utils.translation import ngettext

from .models import CadastroAdocao, RegrasAdocao
from cadastro_animal.models import CadastroAnimal, GaleriaAnimal

class RegrasAdocaoInline(admin.TabularInline):
    model = RegrasAdocao
    fields = ['solicitacao', 'maior_18', 'nao_devolucao', 'ler_contrato']
    max_num = 1  # Limita a apenas uma solicitação por pessoa


class CadastroAdocaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'animal','data_solicitacao_formatada', 'get_solicitacao_status']
    search_fields = ['nome', 'animal__nome']
    list_filter = ['animal__nome', 'data_solicitacao']
    ordering = ['data_solicitacao']
    actions = ['marcar_como_aprovado', 'marcar_como_desaprovar', 'marcar_como_cancelado']  
    
    # Ações personalizadas
    inlines = [RegrasAdocaoInline]  # Inclui o inline de regras de adoção


    @admin.action(description="Aprovar os pedidos selecionados")
    def marcar_como_aprovado(self, request, queryset):
        updated_count = 0
        for adocao in queryset:
            regra_adocao = adocao.regras_adocoes.first()
            if regra_adocao and regra_adocao.solicitacao in ["feito", "cancelado"]:
                animal = adocao.animal
                animal.disponivel = True #marcar o animal como indisponivel
                animal.save() #salvar as alterações do 'animal.disponivel'

                regra_adocao.solicitacao = 'concluido'
                regra_adocao.save() #salvar as alterações da 'adocao.solicitacao'

                updated_count += 1
            
        # Exibe mensagem de erro caso nenhum pedido tenha sido atualizado
        if updated_count == 0:
            self.message_user(request, "Nenhum pedido foi aprovado.", messages.ERROR)
        else:
            # Exibe mensagem de sucesso para a quantidade de pedidos aprovados
            self.message_user(
                request,
                ngettext(
                    '%d pedido aprovado com sucesso!',
                    '%d pedidos aprovados com sucesso!',
                    updated_count,
                ) % updated_count,
                messages.SUCCESS,
            )
            
    @admin.action(description="Desaprovar os pedidos selecionados")
    def marcar_como_desaprovar(self, request, queryset):
        updated_count = 0
        for adocao in queryset:
            regra_adocao = adocao.regras_adocoes.first()
            if regra_adocao and regra_adocao.solicitacao == 'concluido':
                animal = adocao.animal
                animal.disponivel = True #marcar o animal como indisponivel
                animal.save() #salvar as alterações do 'animal.disponivel'

                regra_adocao.solicitacao = 'feito' #mudar o estado para 'em analise' novamente
                regra_adocao.save()
                updated_count += 1
        self.message_user(request, f'{updated_count} pedidos mudados para status "Em análise" com sucesso!')

    @admin.action(description="Cancelar os pedidos os selecionados")
    def marcar_como_cancelado(self, request, queryset):
        updated_count = 0
        for adocao in queryset:
            regra_adocao = adocao.regras_adocoes.first()
            if regra_adocao and regra_adocao.solicitacao in ["feito",  "concluido"]:
                animal = adocao.animal
                animal.disponivel = False #marcar o animal como indisponivel
                animal.save() #salvar as alterações do 'animal.disponivel'

                regra_adocao.solicitacao = 'cancelado'
                regra_adocao.save()
                updated_count += 1
        self.message_user(request, f'{updated_count} pedidos foram mudados para o status "Adoção reprovada" com sucesso!')


admin.site.register(CadastroAdocao, CadastroAdocaoAdmin)
