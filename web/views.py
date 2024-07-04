from django.shortcuts import render, redirect # se importan las funciones
from django.http import HttpResponse #se importa la funcion
from web.postres import postres # se importa la lista
from web.forms import FlanForm, RegisterForm  #se importa el formulario
from web.models import Contact, Flan, UserProfile #se importa la tabla
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.models import User

class LoginViewPropia(SuccessMessageMixin, LoginView):
    success_message = "Has ingresado correctamente"


#def index(req):
    # modo en que se separe la exposicion de flanes publicos y privados
    # flanes_publicos = Flan.objects.filter(is_private=False)
    # context ={
    #     'flanes':flanes_publicos,
    # }
    
    # return render(req, 'index.html', context)


#
def index(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        context = {
            'flanes': []
            }
        if user_profile.user_type == 'free':
            context['flanes'] = Flan.objects.filter(type_flan='free')
        elif user_profile.user_type == 'premium':
            context['flanes'] = Flan.objects.filter(type_flan='free') | Flan.objects.filter(type_flan='premium')
        elif user_profile.user_type == 'diamond':
            context['flanes'] = Flan.objects.filter(type_flan='free') | Flan.objects.filter(type_flan='premium') | Flan.objects.filter(type_flan='diamond')
        return render(request, 'index.html', context)
    else:
        flanes_publicos = Flan.objects.filter(type_flan='free')
        context = {
            'flanes': flanes_publicos,
            }
        return render(request, 'index.html', context)


@login_required
def welcome(req):
    # debe mostros solo los flanes privados de la base de datos
    
    flanes_privados = Flan.objects.filter(is_private=True)
    flanes_publicos = Flan.objects.filter(is_private=False)
    flanes =Flan.objects.all()
    context ={
        'flanes':flanes
    }
    return render(req,'welcome.html', context)

# def detalleFlan(req, id):
#     #print (f'\n\n\n{id}\n\n\n')
#     id = int(id)
#     flan_selec = None
#     for postre in postres:
#         if postre['id'] == id:
#             flan_selec = postre
#             break
#     context = {
#         'postre': flan_selec
#     }
#     return render(req, 'otro.html', context)

def about(req):
    return render(req, 'about.html')




def contact_form(req):
    errores=[]
    
    customer_name = req.POST["customer_name"]
    customer_email = req.POST["customer_email"]
    message = req.POST["message"]
    
    # if len(customer_name  )> 64:
    #     errores.append('largo mayor a 64 caracteres')
    # if not '@' in customer_email:
    #     errores.append('Falta el arroba')
    #     context ={'errores' : errores}
    # if len(errores) > 0:
    #     return render(req, 'welcome.html',context)
    # else:
    #     return render(req, 'exito.html')
        #return redirect ("/nombre_pagina")
    
    
    
    #print(customer_email)
    #return HttpResponse ("Tamos")
    

    #ahora tengo que validar que customer_email tenga al menos una @
    #y customer_name sea de largo maximo 64 
    #
    #si len errores == 0 : redirijo a pagina de exito
    # si len errores > 0 : vuelvo a vargar 'welcome.html', mostrando los errores
    
def contact(req):
    if req.method == 'GET':
        form = FlanForm()
        context={'form':form}
        return render(req, 'contact.html', context)
    else:
        #validar el formulario
        form = FlanForm(req.POST)
        if form.is_valid():
            #Se agrega la funcion de guardado
            Contact.objects.create(
                **form.cleaned_data
            )
            return redirect('/success')
        context ={'form':form}
        
    return render(req, 'contact.html', context)

def success(req):
    return render(req,'exito.html')

# def contact(request):
#     if request.method == 'GET':
#         form = ContactForm()                    # Se crea una instancia del formulario ContactForm sin datos iniciales.
#         context = {'form': form}                # Se crea un contexto que contiene el formulario vacío.
#         return render(request, 'contact.html', context) # Se renderiza la plantilla 'contact.html' con el contexto.
#     else:
#         form = ContactForm(request.POST)        # Se crea una instancia de ContactForm con los datos enviados en la solicitud POST.
#         if form.is_valid():                     # Se verifica si los datos del formulario son válidos.
#             Contact.objects.create(
#                 **form.cleaned_data
#             )                                   # Esta es la forma de pedirle a un modelo que cree un registro usando los datos de un formulario
#             return redirect('/success')         # Si el formulario es válido, se redirige al usuario a la URL '/success'.
#         context = {'form': form}                # Se crea un contexto que contiene el formulario con los datos (válidos o no).
#         return render(request, 'contact.html', context) # Se vuelve a renderizar la plantilla con el contexto actualizado.

# def login(req):
#     return render(req, 'login.html')

def register(req):
    return render(req, 'register.html')


def register_user(request, user_type):
    form = RegisterForm()
    context = {'form': form}
    
    if request.method == 'GET':
        return render(request, f'registration/register{user_type}.html', context)
    
    form = RegisterForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        if data['password'] != data['passRepeat']:
            messages.error(request, 'Ambas contraseñas deben ser iguales')
            return redirect(f'/register{user_type}')
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        UserProfile.objects.create(
            user=user,
            user_type=user_type
        )
        messages.success(request, '¡Usuario creado! por favor, inicie sesión')
        return redirect('/')
    
    context['form'] = form
    return render(request, f'registration/register{user_type}.html', context)

def suscriptions(request):
    return render (request, 'registration/suscriptions.html')


def registerfree(request):
    return register_user(request, 'free')


def registerpremium(request):
    return register_user(request, 'premium')


def registerdiamond(request):
    return register_user(request, 'diamond')

    #agregar funciones para los otros tipos de usuarios