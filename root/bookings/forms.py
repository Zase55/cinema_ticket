from django import forms
from .models import Reserva, Asiento

class ReservaForm(forms.ModelForm):
    asientos = forms.ModelMultipleChoiceField(
        queryset=Asiento.objects.all(), 
        widget=forms.CheckboxSelectMultiple  # Permite seleccionar múltiples asientos
    )

    class Meta:
        model = Reserva
        fields = ['funcion', 'asientos']