from django.db import models
#from django.contrib.auth.models import Usuario


# Create your models here.
from Categoria.models import Categoria
from Users.models import User


class Votaciones(models.Model):

    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank=True)
    votaciones = models.IntegerField(default=1)
    boletin = models.ForeignKey('Boletin',on_delete=models.SET_NULL,null=True, blank=True)

class Boletin(models.Model):
   nombre = models.CharField(max_length=100)
   descripcion = models.CharField(max_length=200)
   imagen =models.URLField(max_length = 200,null=True, blank=True)
   target = models.IntegerField(null=True)
   frecuencia = models.IntegerField(null=True)
   created_at = models.DateField(null=True)
   categorias = models.ManyToManyField(Categoria,blank=True, related_name='categorias')
   owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

   def __str__(self):
      return self.nombre

