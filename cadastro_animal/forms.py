from django import forms
from .models import CadastroAnimal, GaleriaAnimal

class FormCadastroAnimal(forms.ModelForm):
    class Meta:
        model = CadastroAnimal
        fields = "__all__"
