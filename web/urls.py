from django.urls import path
from web.views import index, about, welcome, detalleFlan


urlpatterns =[
    path ('', index),
    path('about/', about),
    path ('welcome/', welcome),
    path('flan/<id>/', detalleFlan)
]