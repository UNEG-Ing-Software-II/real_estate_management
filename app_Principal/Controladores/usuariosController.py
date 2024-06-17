from django.shortcuts import render, get_object_or_404, render, redirect
from django.http import JsonResponse
from app_Principal.models import *
from django.views.decorators.csrf import csrf_exempt
import json


def buscar_propietario(request):
    if request.method == 'GET':
        cedula = request.GET.get('cedula', None)
        inmueble_id = request.GET.get('id_inmueble', None)
        inmueble = Inmueble.objects.get(id=inmueble_id)
        if cedula:
            propietario = Usuario.objects.filter(cedula=cedula, rol="Propietario").first()
            if propietario:
                if InmueblePropietario.objects.filter(persona_id=propietario, inmueble_id=inmueble).exists():
                    return JsonResponse({
                        'cedula': propietario.cedula,
                        'nombre': propietario.nombre,
                        'apellido': propietario.apellido,
                        'correo': propietario.correo,
                        'msg': 'Este propietario ya posee este inmueble',
                        'valido':False,
                    }, status=200)
                else:
                    return JsonResponse({
                        'cedula': propietario.cedula,
                        'nombre': propietario.nombre,
                        'apellido': propietario.apellido,
                        'correo': propietario.correo,
                        'valido':True,
                    }, status=200)
            else:
                return JsonResponse({'error': 'Propietario no encontrado'}, status=404)
        else:
            return JsonResponse({'error': 'Cédula no proporcionada'}, status=400)

@csrf_exempt
def validar_propietario(request):
    if request.method == 'POST':
        cedula = request.POST.get('cedula')
        correo = request.POST.get('correo')

        if Usuario.objects.filter(cedula=cedula).exists():
            return JsonResponse({'error': 'La cédula ya está en uso.'}, status=400)

        if Usuario.objects.filter(correo=correo).exists():
            return JsonResponse({'error': 'El correo ya está en uso.'}, status=400)

        # Retornar una respuesta exitosa en formato JSON
        return JsonResponse({'success': 'Validación exitosa.'})

    return JsonResponse({'error': 'Método no permitido.'}, status=405)
    


@csrf_exempt
def guardar_propietario_inmueble(request):
    if request.method == 'POST':
        cedula = request.POST.get('cedula')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        password = request.POST.get('password', None)
        method = request.POST.get('method')

        
        if method == 'nuevo':
            # Crear un nuevo propietario
            propietario = Usuario.objects.create_user(
                correo=correo,
                nombre=nombre,
                apellido=apellido,
                password=password,
                cedula=cedula,
                rol="Propietario"
            )
        elif method == 'existente':
            propietario = get_object_or_404(Usuario, cedula=cedula, rol="Propietario")

        # Obtener el inmueble y crear la relación
        inmueble = get_object_or_404(Inmueble, id=request.POST.get('inmueble_id'))
        InmueblePropietario.objects.create(persona_id=propietario, inmueble_id=inmueble)

        return redirect('inicio Asesor')

    return JsonResponse({'error': 'Método no permitido'}, status=405)

def eliminar_propietarios(request):
    if request.method == 'POST':
        propietarios_seleccionados = request.POST.getlist('propietarios_seleccionados')
        if propietarios_seleccionados:
            for relacion_id in propietarios_seleccionados:
                InmueblePropietario.objects.filter(id=relacion_id).delete()
            
        # Retorna una respuesta exitosa si se eliminaron los propietarios correctamente
        return redirect('inicio Asesor')

    return JsonResponse({'error': 'Método no permitido'}, status=405)
