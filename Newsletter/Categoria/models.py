from django.db import models


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    created_at= models.DateField(null=True)

    def __str__(self):
        return self.nombre