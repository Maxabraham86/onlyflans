from django.urls import path
from web.views import index, about, welcome, detalleFlan, contact, success


urlpatterns =[
    path ('', index),
    path('about/', about),
    
    path ('welcome/', welcome, name="welcome"),
    #path('flan/<id>/', detalleFlan, name="flan id"),
    # path('contact_form/', contact_form, name="contact form" ),
    path('contact/', contact, name="contact form" ),
    path('success/', success, name='exito')
]