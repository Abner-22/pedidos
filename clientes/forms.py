from django import forms
from clientes.models import Cliente

class Cliente_forms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Cliente
