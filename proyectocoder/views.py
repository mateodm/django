from django.shortcuts import render, redirect, get_object_or_404
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

def editar_gorra(request, id):
    gorra = get_object_or_404(Gorras, id=id)

    if request.method == 'POST':
        form = GorraForm(request.POST, instance=gorra)
        if form.is_valid():
            form.save()
            return redirect('../../gorras')  
    else:
        form = GorraForm(instance=gorra)

    return render(request, 'editar_gorra.html', {'form': form, 'gorra': gorra})

def borrar_gorra(request, id):
    gorra = get_object_or_404(Gorras, id=id)

    if request.method == 'POST':
        gorra.delete()
        return redirect('../../gorras')  

    return render(request, 'borrar_gorra.html', {'gorra': gorra})

def post_calzado(request):
    if request.method == 'POST':
        form = CalzadoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "calzado.html")
    else:
        form = CalzadoForm()
    return render(request, 'calzado.html', {'form': form})
def editar_calzado(request, id):
    calzado = get_object_or_404(Calzado, id=id)

    if request.method == 'POST':
        form = CalzadoForm(request.POST, instance=calzado)
        if form.is_valid():
            form.save()
            return redirect('../../calzado')  
    else:
        form = CalzadoForm(instance=calzado)

    return render(request, 'editar_calzado.html', {'form': form, 'calzado': calzado})

def borrar_calzado(request, id):
    calzado = get_object_or_404(Calzado, id=id)

    if request.method == 'POST':
        calzado.delete()
        return redirect('../../calzado')  

    return render(request, 'borrar_calzado.html', {'calzado': calzado})

def post_remeras(request):
    if request.method == 'POST':
        form = RemeraForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "remeras.html")
    else:
        form = RemeraForm()
    return render(request, 'remeras.html', {'form': form})

def editar_remera(request, id):
    remera = get_object_or_404(Remeras, id=id)

    if request.method == 'POST':
        form = RemeraForm(request.POST, instance=remera)
        if form.is_valid():
            form.save()
            return redirect('../../remeras')  
    else:
        form = RemeraForm(instance=remera)

    return render(request, 'editar_remera.html', {'form': form, 'remera': remera})

def borrar_remera(request, id):
    remera = get_object_or_404(Remeras, id=id)

    if request.method == 'POST':
        remera.delete()
        return redirect('../../remeras')  

    return render(request, 'borrar_remera.html', {'remera': remera})

def search_remeras(request):
    if request.method == "GET":
        input = request.GET["nombre"]
        result = Remeras.objects.filter(nombre__icontains=input)
        return render(request, 'find_remeras.html', {'result': result, 'input': input})
    
def search_gorras(request):
        if request.method == "GET":
            input = request.GET["nombre"]
            result = Gorras.objects.filter(nombre__icontains=input)
            return render(request, 'find_gorras.html', {'result': result, 'input': input})
    
def search_calzado(request):
        if request.method == "GET":
            input = request.GET["modelo"]
            result = Calzado.objects.filter(modelo__icontains=input)
            return render(request, 'find_calzado.html', {'result': result, 'input': input})



