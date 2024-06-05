from django.shortcuts import render
from web.postres import postres


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