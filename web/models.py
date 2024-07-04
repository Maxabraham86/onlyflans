from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Contact(models.Model):
    nombre= models.CharField(max_length = 64)
    email= models.EmailField(max_length = 30)
    mensaje= models.CharField(max_length = 255)
    
    
class Flan(models.Model):
    FLAN_TYPE_CHOICES = (
        ('free', 'Free'),
        ('premium', 'Premium'),
        ('diamond', 'Diamond'),
    )
    uuid = models.UUIDField(editable =False, default =uuid.uuid4)
    nombre = models.CharField(max_length=64 )
    descripcion = models.TextField()
    precio = models.IntegerField(default=1000)
    foto = models.URLField()
    is_private = models.BooleanField(default=False)
    type_flan = models.CharField(max_length=10, choices=FLAN_TYPE_CHOICES, default='free')
    def __str__(self):
        return self.nombre
    
    
class UserProfile(models.Model):
    USER_TYPE_CHOICES=(
        ('free', 'Free'),
        ('premium', 'Premium'),
        ('diamond', 'Diamond')
    )
    user=models.OneToOneField(User, on_delete = models.CASCADE)
    user_type=models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    
    
    def __str__(self):
        return self.user.username