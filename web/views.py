from django.shortcuts import render, redirect
from django.http import HttpResponse
from web.postres import postres
from web.forms import FlanForm

def index(req):
    context ={
        'postres':postres
    }
    
    return render(req, 'index.html', context)

def detalleFlan(req, id):
    #print (f'\n\n\n{id}\n\n\n')
    id = int(id)
    flan_selec = None
    for postre in postres:
        if postre['id'] == id:
            flan_selec = postre
            break
    context = {
        'postre': flan_selec
    }
    return render(req, 'otro.html', context)

def about(req):
    return render(req, 'about.html')



def welcome(req):
    
    
    return render(req, 'welcome.html')

def contact_form(req):
    errores=[]
    
    customer_name = req.POST["customer_name"]
    customer_email = req.POST["customer_email"]
    message = req.POST["message"]
    
    if len(customer_name  )> 64:
        errores.append('largo mayor a 64 caracteres')
        
    
    if not '@' in customer_email:
        errores.append('Falta el arroba')

        context ={'errores' : errores}
    if len(errores) > 0:
        return render(req, 'welcome.html',context)
    else:
        return render(req, 'exito.html')
    
    
        #return redirect ("/nombre_pagina")
    
    
    
    
    print(customer_email)
    #return HttpResponse ("Tamos")
    

    #ahora tengo que validar que customer_email tenga al menos una @
    #y customer_name sea de largo maximo 64 
    #
    #si len errores == 0 : redirijo a pagina de exito
    # si len errores > 0 : vuelvo a vargar 'welcome.html', mostrando los errores
    
def formd(req):
    if req.method == 'GET':
        form = FlanForm()
        context={'form':form}
        return render(req, 'welcome.html', context)
    else:
        #validar el formulario
        form = FlanForm(req.POST)
        if form.is_valid():
            return redirect('/succes')
        context ={'form':form}
        
    return render(req, 'welcome.html', context)

def succes(req):
    return render(req,'exito.html')
