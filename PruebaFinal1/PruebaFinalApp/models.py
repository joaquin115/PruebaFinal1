from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Persona(models.Model):

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha = models.DateField(max_length=20)

class Publicaciones(models.Model):
    imagen = models.ImageField(null=True, blank=True)
    pais = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_viaje = models.DateField()
    autor = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL) 

    class Meta:
        verbose_name_plural = "Publicaciones"
        db_table = "imageupload"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='media', null=True, blank=True)