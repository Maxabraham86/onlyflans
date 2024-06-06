from django.urls import path
from web.views import index, about, welcome, detalleFlan, contact_form


urlpatterns =[
    path ('', index),
    path('about/', about),
    path ('welcome/', welcome, name="welcome"),
    path('flan/<id>/', detalleFlan, name="flan id"),
    path('contact_form', contact_form, name="contact form" )
]