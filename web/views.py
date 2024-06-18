from django.shortcuts import render, redirect # se importan las funciones
from django.http import HttpResponse #se importa la funcion
from web.postres import postres # se importa la lista
from web.forms import FlanForm  #se importa el formulario
from web.models import Contact, Flan #se importa la tabla
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView


class LoginViewPropia(SuccessMessageMixin, LoginView):
    success_message = "Has ingresado correctamente"


def index(req):

    flanes_publicos = Flan.objects.filter(is_private=False)
    context ={
        'flanes':flanes_publicos,
    }
    
    return render(req, 'index.html', context)

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