from django.db import models
from django.utils import timezone

from cadastro_animal.models import CadastroAnimal


class CadastroAdocao(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    animal = models.ForeignKey(CadastroAnimal, on_delete=models.CASCADE, related_name="adocoes")

    data_solicitacao = models.DateTimeField(auto_now_add=True)  # Data da solicitação de adoção

    def __str__(self):
        return f"Adoção de {self.animal.nome} por {self.nome}"
    
class RegrasAdocao(models.Model):
    maior_18 = models.BooleanField(default=True)
    nao_devolucao = models.BooleanField(default=True)
    ler_contrato = models.BooleanField(default=True)

    adocao = models.ForeignKey(CadastroAdocao, on_delete=models.CASCADE, related_name="regras_adocoes")