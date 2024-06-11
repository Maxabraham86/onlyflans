from django.db import models
import uuid
# Create your models here.
class Contact(models.Model):
    nombre= models.CharField(max_length = 64)
    email= models.EmailField(max_length = 30)
    mensaje= models.CharField(max_length = 255)
    
    
class Flan(models.Model):
    
    uuid = models.UUIDField(editable =False, default =uuid.uuid4)
    nombre = models.CharField(max_length=64 )
    descripcion = models.TextField()
    precio = models.IntegerField(default=1000)
    foto = models.URLField()
    is_private = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre