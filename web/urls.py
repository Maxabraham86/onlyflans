from django.urls import path
from web.views import index, about, welcome


urlpatterns =[
    path ('', index),
    path('about/', about),
    path ('welcome/', welcome)
    
]