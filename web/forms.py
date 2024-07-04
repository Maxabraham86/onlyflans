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
        max_length=50,
        label='Usuario:',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 fst-italic',
            'placeholder': 'Ingrese el usuario aquí'
        })
    )
    email = forms.EmailField(
        max_length=100,
        label='Email:',
        widget=forms.EmailInput(attrs={
            'class': 'form-control mb-3 fst-italic',
            'placeholder': 'Ingrese su email aquí'
        })
    )
    password = forms.CharField(
        max_length=50,
        label='Contraseña:',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-3 fst-italic',
            'placeholder': 'Ingrese la contraseña aquí'
        })
    )
    passRepeat = forms.CharField(
        max_length=50,
        label='Repita la Contraseña:',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-3 fst-italic',
            'placeholder': 'Repita la Contraseña aquí'
        })
    )