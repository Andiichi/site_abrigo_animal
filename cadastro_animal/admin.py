from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib import messages

from .models import CadastroAnimal, GaleriaAnimal

class AnimalImagemInline(admin.TabularInline):
    model = GaleriaAnimal

class CadastroAnimalAdmin(admin.ModelAdmin):
    list_display = ['nome', 'especie', 'data_criacao', 'sexo', 'image_tag', 'adocao_tag']  # Adiciona a exibição da imagem
    search_fields = ['nome']  # Campos que podem ser pesquisados
    list_filter = ['especie', 'sexo', 'disponivel']  # Filtros disponíveis na barra lateral
    ordering = ['nome']  # Ordenação por nome

    inlines = [AnimalImagemInline]

    # Função para deletar a imagem
    def delete_image(self, request, obj):
        if obj.imagem:
            obj.delete_image()  # Chama o método delete_image do modelo
            self.message_user(request, "Imagem deletada com sucesso.", messages.SUCCESS)
        else:
            self.message_user(request, "Este animal não possui imagem.", messages.WARNING)

    delete_image.short_description = 'Deletar Imagem'

    # Função para criar o botão de deletar imagem no Django Admin
    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path('<int:pk>/delete_image/', self.admin_site.admin_view(self.delete_image), name='animal-delete-image'),
        ]
        return custom_urls + urls

    # Campo customizado para adoção
    def adocao_tag(self, obj):
        return obj.disponivel
    
    adocao_tag.boolean = True
    adocao_tag.short_description = 'Disponível para adoção'

    # Exibir a primeira imagem associada ao animal
    def image_tag(self, obj):
        # Obtém a primeira imagem associada ao animal
        primeira_imagem = GaleriaAnimal.objects.filter(animal=obj).first()
        if primeira_imagem and primeira_imagem.imagem:
            return mark_safe(f'<img src="{primeira_imagem.imagem.url}" style="width: 100px; height: auto;" />')
        return "Sem imagem"
    
    image_tag.short_description = 'Imagem'


    # Ações personalizadas para alterar o sexo do animal
    @admin.action(description="Alterar sexo para Fêmea")
    def marcar_como_femea(self, request, queryset):
        machos = queryset.filter(sexo="macho")
        updated = machos.update(sexo="femea")
        self.message_user(request, f'{updated} animal(is) marcado(s) como Fêmea.')

    @admin.action(description="Alterar sexo para Macho")
    def marcar_como_macho(self, request, queryset):
        femeas = queryset.filter(sexo="femea")
        updated = femeas.update(sexo="macho")
        self.message_user(request, f'{updated} animal(is) marcado(s) como Macho.')

    actions = [marcar_como_macho, marcar_como_femea]


admin.site.register(CadastroAnimal, CadastroAnimalAdmin)