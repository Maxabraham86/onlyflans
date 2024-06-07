from django import forms

class FlanForm(forms.Form):
    nombre = forms.CharField (
        max_length=10,
        label='Escribe tu nombre',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'})
    )
    
    email = forms.EmailField(
        max_length=15,
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Ingrese Correo Electrónico'})
    )
    mensaje = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Mensaje', "rows":6})
    )