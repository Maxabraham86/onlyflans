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
    
    
class LogingForm(forms.Form):
    username = forms.CharField(
        max_length =25,
        label= 'usuario', 
        widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mensaje'})
    )
    password = forms.CharField(
        max_length =25,
        label='password',
        widget = forms.PasswordInput
    )
    
    #forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    
    class RegisterForm(forms.Form):
        username = forms.CharField(
            max_length =25,
            label= 'usuario', 
            widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mensaje'})
        )
        password = forms.CharField(
            max_length =25,
            label='password',
            widget = forms.PasswordInput
        )
        passrepeat = forms.CharField(
        max_length =25,
        label='password',
        widget = forms.PasswordInput
    )