from django.db import models
from django.utils import timezone

from cadastro_animal.models import CadastroAnimal


class CadastroAdocao(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=150)
    animal = models.ForeignKey(CadastroAnimal, on_delete=models.CASCADE, related_name="adocoes")
    data_solicitacao = models.DateTimeField(auto_now_add=True)  # Data da solicitação de adoção

    
    def get_solicitacao_status(self):
        regra_adocao = self.regras_adocoes.first()  # Obtém o primeiro registro relacionado em RegrasAdocao
        return regra_adocao.get_solicitacao_display() if regra_adocao else "Não especificado"
    get_solicitacao_status.short_description = "Status da Solicitação"  # Nome da coluna no Django Admin


    def data_solicitacao_formatada(self):
        return self.data_solicitacao.strftime("%d/%m/%Y")
    data_solicitacao_formatada.short_description = "Data da Solicitação" #nome da coluna no admin

    class Meta:
        verbose_name = 'Cadastro de Adoção'
        verbose_name_plural = 'Cadastro de Adoções'
        ordering = ['-nome']

    def __str__(self):
        return f"Solicitação de adoção do '{self.animal.nome}' por '{self.nome}' feita!"
    

    
class RegrasAdocao(models.Model):
    STATUS = [
        ('feito', 'Em analise'),
        ('concluido', 'Adoção aprovada'),
        ('cancelado', 'Adoção reprovada'),
    ]

    solicitacao = models.CharField(max_length=10, choices=STATUS, default='feito')
    maior_18 = models.BooleanField(default=True)
    nao_devolucao = models.BooleanField(default=True)
    ler_contrato = models.BooleanField(default=True)

    adocao = models.ForeignKey(CadastroAdocao, on_delete=models.CASCADE, related_name="regras_adocoes")