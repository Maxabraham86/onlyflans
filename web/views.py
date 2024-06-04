from django.shortcuts import render

# postres =[
#     { 'id' : 1,
#     'nombre': 'leche asada',
#     'ingrediente' :'leche, huevo...'
    
# },
#     {'id' :2,
#     'nombre': 'flan de coco',
#     'ingrediente' :'leche, coco...'
# },
#     {'id':3
#     'nombre': 'flan de chocolate',
#     'ingrediente' :'leche, chocolate...'}
#         ]

# Create your views here.
def index(req):
    context = {
        'leche asada':'leche asada',
        'flan de coco': 'flan con coco'
    }
        
    
    
    return render(req, 'index.html',context)


def about(req):
    return render(req, 'about.html')



def welcome(req):
    return render(req, 'welcome.html')