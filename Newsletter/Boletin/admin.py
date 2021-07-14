from django.contrib import admin

# Register your models here.

from Boletin.models import  Boletin,Votaciones

admin.site.register(Boletin)
admin.site.register(Votaciones)
