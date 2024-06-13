from django.urls import path
from web.views import index, about, welcome, contact, success, register
from django.contrib.auth import views as auth_views

urlpatterns =[
    path ('', index),
    path('about/', about),
    path ('welcome/', welcome, name="welcome"),
    #path('flan/<id>/', detalleFlan, name="flan id"),
    # path('contact_form/', contact_form, name="contact form" ),
    path('contact/', contact, name="contact form" ),
    path('success/', success, name='exito'),
    #path('login/', login, name='login'),
    path('register/', register, name='registro'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]