from django import forms
from .models import comentarios



class FormUser(forms.ModelForm):
    class Meta:
        model = comentarios
        fields = '__all__'

class prodForm(forms.Form):
    title = forms.CharField(label="Titulo",max_length=255, min_length=3, required=True)
    description = forms.CharField(label="descripcion", widget=forms.Textarea(attrs={'row':5, 'cols':20} ))
    price = forms.FloatField(label="precio",min_value=0.1)
