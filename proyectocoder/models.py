from django.db import models

class Remeras(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    talle = models.CharField(max_length=3)
    color = models.CharField(max_length=10)

class Calzado(models.Model):
    modelo = models.CharField(max_length=20)
    precio = models.IntegerField()
    talle = models.IntegerField()
    estado = models.CharField(max_length=10)

class Gorras(models.Model):
    nombre = models.CharField(max_length=40)
    color = models.CharField(max_length=20)
    precio = models.IntegerField()
