from django.shortcuts import render
from django.http import HttpResponse
from proyectocoder.models import *

def ver_remeras(req):
    remeras = Remeras.objects.all()
    all = {"remeras": remeras}
    return render(req, "remeras.html", all)
def ver_gorras(req):
    gorras = Gorras.objects.all()
    all = {"gorras": gorras}
    return render(req, "gorras.html", all)
def ver_calzado(req):
    calzado = Calzado.objects.all()
    all = {"calzados": calzado}
    return render(req, "calzado.html", all)

def agregar_remeras(req):
    nombre = req.nombre
    precio = req.precio
    talle = req.talle
    color = req.color
    remeras = Remeras(nombre= nombre, precio= precio, talle= talle, color= color)
    remeras.save()
    return HttpResponse("Remera añadida a la db")
