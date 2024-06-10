# forms.py
import shutil
from django import forms
from app_Principal.models import *
from django.contrib.auth.decorators import login_required
from MyR.backend import role_required     
import json

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            'tipoPropiedad', 'precio', 'niveles', 'metros_terreno', 
            'metros_construccion', 'bathroom', 'cuarto_servicio', 
            'oficina', 'estacionamiento', 'half_bath', 'terraza', 
            'habitacion', 'maletero', 'estado', 'direccion',
            'latitud', 'longitud'
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
    return redirect('inicio Asesor')

@login_required(login_url='login')
@role_required('Asesor')
def modificar_inmueble(request, inmueble_id):
    # Obtener el inmueble por su ID
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            #Nuevas Imagenes
            fotos = request.FILES.getlist('fotos')
            for foto in fotos:
                imagen_inmueble = Imagen_inmueble()
                imagen_inmueble.inmueble = inmueble
                imagen_inmueble.foto = foto
                imagen_inmueble.save()
            
            #Imágenes eliminadas
            deleted_images = request.POST.get('deletedImages')
            if deleted_images:
                deleted_images = json.loads(deleted_images)
                for image_id in deleted_images:
                    try:
                        image = Imagen_inmueble.objects.get(id=image_id)
                        
                        if image.foto and os.path.isfile(image.foto.path):
                            os.remove(image.foto.path)
                        
                        image.delete()
                    except Imagen_inmueble.DoesNotExist:
                        continue
            return redirect('inicio Asesor')
    return redirect('inicio Asesor')


@login_required(login_url='login')
@role_required('Asesor')
def eliminar_inmueble(request, inmueble_id):
    # Obtener el inmueble por su ID
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    if request.method == 'POST':
        imagenes = Imagen_inmueble.objects.filter(inmueble=inmueble)
        if imagenes.exists():
            image_path = os.path.dirname(imagenes.first().foto.path)
            if os.path.isdir(image_path):
                shutil.rmtree(image_path)
        imagenes.delete()
        inmueble.delete()
        return redirect('inicio Asesor')
    return redirect('inicio Asesor')


def inmuebles_registrados(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'inmuebles_registrados.html', {'inmuebles': inmuebles})





