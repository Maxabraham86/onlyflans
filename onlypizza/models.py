from django.db import models
import uuid
# Create your models here.
class Pizza(models.Model):
    uuid= models.UUIDField(editable =False, default =uuid.uuid4)
    nombre = models.CharField(max_length=64 )
    descripcion= models.Texfield()
    precio =models.IntegeField(default=1000)
    foto = models.URLField()
    is_private = models.BooleanField(default=False)
    
    