# forms.py
from django import forms
from app_Principal.models import *
from django.contrib.auth.decorators import login_required
from MyR.backend import role_required     
        
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
@login_required(login_url='login')
@role_required('Asesor')
def registrar_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio Asesor')
    return redirect('inicio_Asesor')

@login_required(login_url='login')
@role_required('Asesor')
def modificar_inmueble(request, inmueble_id):
    # Obtener el inmueble por su ID
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('inicio Asesor')
    return redirect('inicio_Asesor')

@login_required(login_url='login')
@role_required('Asesor')
def eliminar_inmueble(request, inmueble_id):
    # Obtener el inmueble por su ID
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    if request.method == 'POST':
        inmueble.delete()
        return redirect('inicio Asesor')
    return redirect('inicio_Asesor')

def inmuebles_registrados(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'inmuebles_registrados.html', {'inmuebles': inmuebles})





