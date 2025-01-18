from django import forms
from .models import OrdemServico

class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        fields = ['cliente', 'descricao', 'status']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
