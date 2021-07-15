
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre