from django.db import models
from django.utils import timezone

# Create your models here.

class Cliente(models.Model):
	Nombre_cliente= models.CharField(max_length=50)
	Rut = models.CharField(max_length=10)
	Direccion = models.TextField()
	Ciudad = models.CharField(max_length=50)
	Comuna = models.CharField(max_length=50)
	Telefono = models.IntegerField()
	Email = models.EmailField()

	def __str__(self):
		return self.Rut


class Orden(models.Model):
	Nombre_cliente = models.CharField(max_length=50)
	Fecha = models.DateTimeField()
	Hora_inicio = models.TimeField()
	Hora_fin = models.TimeField()
	Codigo_ascensor = models.CharField(max_length=50)
	Modelo_ascensor = models.CharField(max_length=50)
	Fallas = models.TextField()
	Reparaciones = models.TextField()
	Piezas_cambiadas = models.TextField()
	Nombre_cliente = models.CharField(max_length=50)

	def __str__(self):
		return self.Nombre_cliente

class Tecnico(models.Model):
	Nombre_Tecnico = models.CharField(max_length=50)
	Email = models.EmailField()
	Contraseña = models.CharField(max_length=50)

	def __str__(self):
		return self.Email

		
