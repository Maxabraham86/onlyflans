from django.urls import path
from web.views import index, about, welcome


urlpattern =[
    path ('', index),
    path('about/', about),
    path ('welcome/', welcome)
    
]