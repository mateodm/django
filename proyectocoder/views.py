from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from proyectocoder.models import *
from proyectocoder.forms import *

def inicio(req):
    return render(req, "index.html")
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

def post_gorras(request):
    if request.method == 'POST':
        form = GorraForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "gorras.html")
    else:
        form = GorraForm()
    return render(request, 'gorras.html', {'form': form})

def post_calzado(request):
    if request.method == 'POST':
        form = CalzadoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "calzado.html")
    else:
        form = CalzadoForm()
    return render(request, 'calzado.html', {'form': form})

def post_remeras(request):
    if request.method == 'POST':
        form = RemeraForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "remeras.html")
    else:
        form = RemeraForm()
    return render(request, 'remeras.html', {'form': form})


