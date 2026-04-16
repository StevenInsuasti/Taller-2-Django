from django import forms
from .models import Solicitud


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '__all__'
        widgets = {
            'fecha_solicitud': forms.DateInput(attrs={'type': 'date'}),
            'descripcion_detallada': forms.Textarea(attrs={'rows': 4}),
        }
