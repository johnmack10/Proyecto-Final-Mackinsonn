from django.db import models
from django.contrib.auth.models import User

class Jugador(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    fecha_nacimiento = models.DateField(null=True)
    telefono = models.CharField(max_length=20)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   
    
    
    def __str__(self):
        return f"{self.apellido, self.nombre}"

class Torneo(models.Model):
    nombre_torneo = models.CharField(max_length=256)
    ciudad = models.CharField(max_length=256,blank = True)
    fecha_comienzo = models.DateField()
    superficie = models.CharField(max_length=256, blank = True)
    modalidad = models.CharField(max_length=256, blank = True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.nombre_torneo, self.fecha_comienzo}"
    

class Ranking(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    cantidad_puntos = models.PositiveIntegerField()
    torneos_jugados = models.PositiveIntegerField()
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.nombre} contiene {self.cantidad_puntos} puntos"
    

