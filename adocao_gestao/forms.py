from django import forms
from django.core.validators import RegexValidator

from cadastro_animal.models import CadastroAnimal

from .models import  CadastroAdocao, RegrasAdocao

class FormCadastroAdocao(forms.ModelForm):
    # Checkbox fields para as regras de adoção
    maior_18 = forms.BooleanField(
        required=True,
        label="Sou maior de 18 anos",
        help_text="<br><small>Você deve ter pelo menos 18 anos para adotar um animal.</small>"
    )
    nao_devolucao = forms.BooleanField(
        required=True,
        label="Concordo em não devolver o animal",
        help_text="<br><small>Uma vez adotado, o animal deve ser mantido em seu lar para sempre.</small>"
    )
    ler_contrato = forms.BooleanField(
        required=True,
        label="Li e aceito o contrato de adoção",
        help_text="<br><small>É importante que você leia e compreenda o contrato antes de adotar.</small>"
    )

    class Meta:
        model = CadastroAdocao
        fields = ['nome', 'telefone', 'email', 'animal']  # Campos principais

        # Define o estilo dos widgets
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Digite seu nome completo',
                'class': 'form-control'
            }),
            'telefone': forms.TextInput(attrs={
                'placeholder': 'Digite seu telefone com DDD',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Digite seu email',
                'class': 'form-control'
            }),
            'animal': forms.Select(attrs={'class': 'form-select text-capitalize'}),
        }

        labels = {
            'nome': 'Nome Completo',
            'telefone': 'Telefone',
            'email': 'Email',
            'animal': 'Selecione o animal'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtra os animais disponíveis para adoção no campo `animal`
        self.fields['animal'].queryset = CadastroAnimal.objects.filter(disponivel=True)

    def save(self, commit=True):
        # Salva o formulário de adoção
        adocao = super().save(commit=False)
        if commit:
            adocao.save()
            # Salva as regras vinculadas à adoção
            RegrasAdocao.objects.create(
                adocao=adocao,
                maior_18=self.cleaned_data['maior_18'],
                nao_devolucao=self.cleaned_data['nao_devolucao'],
                ler_contrato=self.cleaned_data['ler_contrato']
            )
        return adocao
