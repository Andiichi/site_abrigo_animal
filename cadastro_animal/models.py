from django.db import models
import os
from django.conf import settings
from django.utils import timezone


def upload_to_image(instance, filename):
    # Verificar se a instância é do tipo CadastroAnimal
    if isinstance(instance, CadastroAnimal):
        # Verificar se a instância já foi salva e tem um ID
        if instance.id:
            # Formatar o caminho com ID e nome em minúsculo
            return os.path.join('galeria', instance.nome.lower(), f'{instance.id}_{instance.nome.lower()}_{filename}')
        else:
            # Caso o ID ainda não esteja disponível, salvar apenas com o nome
            return os.path.join('galeria', instance.nome.lower(), filename)
    
    # Verificar se a instância é do tipo GaleriaAnimal (relacionada ao CadastroAnimal)
    elif hasattr(instance, 'animal') and isinstance(instance.animal, CadastroAnimal):
        # Se o ID do animal está disponível
        if instance.animal.id:
            return os.path.join('galeria', instance.animal.nome.lower(), f'{instance.animal.id}_{instance.animal.nome.lower()}_{filename}')
        else:
            return os.path.join('galeria', instance.animal.nome.lower(), filename)
    
    return os.path.join('galeria', 'default', filename)



class CadastroAnimal(models.Model):
    SEXO_CHOICES = [
        ('macho', 'Macho'),
        ('fêmea', 'Fêmea'),
    ]
    ESPECIE_CHOICES = [
        ('cachorro', 'Cachorro'),
        ('gato', 'Gato'),
    ]

    nome = models.CharField(max_length=75)
    idade = models.PositiveIntegerField()
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES, default='macho')
    especie = models.CharField(max_length=10, choices=ESPECIE_CHOICES, default='cachorro')
    disponivel = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = 'Cadastro de Animal'
        verbose_name_plural = 'Cadastro de Animais'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class GaleriaAnimal(models.Model):
    animal = models.ForeignKey(CadastroAnimal, on_delete=models.CASCADE, related_name='galeria')
    imagem = models.ImageField(upload_to=upload_to_image, blank=True, null=True)


    def __str__(self):
        return f'Imagem de {self.animal.nome}'