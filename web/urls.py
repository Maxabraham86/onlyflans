from django.urls import path
from web.views import index, about, welcome, detalleFlan, contact_form, formd, success


urlpatterns =[
    path ('', index),
    path('about/', about),
    path ('welcome/', formd, name="welcome"),
    path('flan/<id>/', detalleFlan, name="flan id"),
    # path('contact_form/', contact_form, name="contact form" ),
    path('contact_form/', formd, name="contact form" ),
    path('success/', success, name='exito')
]