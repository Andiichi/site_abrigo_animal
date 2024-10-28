from django import forms

from .models import CadastroAnimal, GaleriaAnimal


class FormCadastroAnimal(forms.ModelForm):
    class Meta:
        model = CadastroAnimal
        fields = ['nome', 'idade', 'sexo', 'especie']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do animal'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Idade do animal'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'especie': forms.Select(attrs={'class': 'form-select'}),
        }


class GaleriaAnimalForm(forms.ModelForm):
    class Meta:
        model = GaleriaAnimal
        fields = ['imagem']