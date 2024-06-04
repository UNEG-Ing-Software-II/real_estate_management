# forms.py
from django import forms
from app_Principal.models import *

class InmuebleFormPrueba(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            'tipoPropiedad', 'precio', 'niveles', 'metros_terreno', 
            'metros_construccion', 'estado'
        ]
        
class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            'tipoPropiedad', 'precio', 'niveles', 'metros_terreno', 
            'metros_construccion', 'bathroom', 'cuarto_servicio', 
            'oficina', 'estacionamiento', 'half_bath', 'terraza', 
            'habitacion', 'maletero', 'estado', 'ubicacion'
        ]


# views.py
from django.shortcuts import render, redirect, get_object_or_404

def registrar_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inmuebles registrados')

def modificar_inmueble(request, inmueble_id):
    # Obtener el inmueble por su ID
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    if request.method == 'POST':
        form = InmuebleFormPrueba(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('inicio Asesor')
            #return redirect('inmuebles registrados')

def eliminar_inmueble(request, inmueble_id):
    # Obtener el inmueble por su ID
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    if request.method == 'POST':
        inmueble.delete()
        return redirect('')

def inmuebles_registrados(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'inmuebles_registrados.html', {'inmuebles': inmuebles})





