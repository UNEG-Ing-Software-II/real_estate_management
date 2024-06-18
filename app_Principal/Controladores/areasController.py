from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from MyR.backend import role_required
from app_Principal.models import *
import json

def registrar_area(request):
    if request.method == 'POST':
        # Obtener el área seleccionada desde el formulario
        tipo_area = request.POST.get('tipo_area')

        # Obtener las características seleccionadas desde el formulario
        caracteristicas_seleccionadas = request.POST.getlist('caracteristicas')

        # Obtener el inmueble asociado 
        inmueble_id = request.POST.get('inmueble_id')
        inmueble = Inmueble.objects.get(pk=inmueble_id)

        # Crear el área 
        area = Area.objects.create(tipo=tipo_area, inmueble=inmueble)

        # Asociar las características seleccionadas al área
        for nombre_caracteristica in caracteristicas_seleccionadas:
            caracteristica = Caracteristica.objects.get(nombre=nombre_caracteristica, tipo=tipo_area)
            Area_caracteristicas.objects.create(area=area, caracteristica=caracteristica).save()

        # Guardar el área en la base de datos
        area.save()
        inmueble_id = request.POST.get('inmueble_id')
        return redirect('inmueble_detalles', inmueble_id=inmueble_id)
    return redirect('inicio Asesor')

def eliminar_area(request, area_id):
    if request.method == 'POST':
        area = get_object_or_404(Area, id=area_id)
        area.delete()
        inmueble_id = request.POST.get('inmueble_id')
        return redirect('inmueble_detalles', inmueble_id=inmueble_id)
    return redirect('inicio Asesor')

def modificar_area(request, area_id):
    if request.method == 'POST':
        area = get_object_or_404(Area, id=area_id)
        inmueble_id = request.POST.get('inmueble_id')
        
        # Limpiar las características actuales
        area.area_caracteristicas_set.all().delete()

        # Obtener las características seleccionadas desde el formulario
        caracteristicas_seleccionadas = request.POST.getlist('caracteristicas')

        # Asociar las nuevas características seleccionadas al área
        for nombre_caracteristica in caracteristicas_seleccionadas:
            caracteristica = Caracteristica.objects.get(nombre=nombre_caracteristica, tipo=area.tipo )
            Area_caracteristicas.objects.create(area=area, caracteristica=caracteristica).save()

        # Guardar el área en la base de datos
        area.save()

        return redirect('inmueble_detalles', inmueble_id=inmueble_id)

    return redirect('inicio Asesor')


def scrip_llenado_caracteristicas(request):
    if request.method == 'POST':
        inmueble_id = request.POST.get('inmueble_id')
        areas_json = '''
        [
            {
                "tipo": "Cocina",
                "caracteristicas": [
                    {"nombre": "Vitrocerámica"},
                    {"nombre": "Eléctrica"},
                    {"nombre": "Gas"},
                    {"nombre": "Encimera"},
                    {"nombre": "Mampostería"},
                    {"nombre": "Horno"},
                    {"nombre": "Microondas"},
                    {"nombre": "Salpicadero"},
                    {"nombre": "Filtro de agua"},
                    {"nombre": "Campana"},
                    {"nombre": "Freezer"},
                    {"nombre": "Nevera"},
                    {"nombre": "Lavadora"},
                    {"nombre": "Secadora"}
                ]
            },
            {
                "tipo": "Sala",
                "caracteristicas": [
                    {"nombre": "Mesa"},
                    {"nombre": "Sillas"},
                    {"nombre": "A/A"},
                    {"nombre": "Vitrina"},
                    {"nombre": "Cantv"},
                    {"nombre": "Internet"},
                    {"nombre": "Televisor"},
                    {"nombre": "Directv"},
                    {"nombre": "Sofa"},
                    {"nombre": "Poltrona"},
                    {"nombre": "Biblioteca"},
                    {"nombre": "Lamparas"}
                ]
            },
            {
                "tipo": "Dormitorio Principal",
                "caracteristicas": [
                    {"nombre": "Camas"},
                    {"nombre": "Colchon"},
                    {"nombre": "Peinadora"},
                    {"nombre": "Vestier"},
                    {"nombre": "A/A"},
                    {"nombre": "Mesa noche"},
                    {"nombre": "Poltrona"},
                    {"nombre": "Closet"},
                    {"nombre": "Espejo"},
                    {"nombre": "H. Theater"},
                    {"nombre": "Perchero"}
                ]
            },
            {
                "tipo": "Cuarto",
                "caracteristicas": [
                    {"nombre": "Camas"},
                    {"nombre": "Literas"},
                    {"nombre": "Colchon"},
                    {"nombre": "Mesa"},
                    {"nombre": "Lámparas"},
                    {"nombre": "Peinadora"},
                    {"nombre": "Vestier"},
                    {"nombre": "Closeth"},
                    {"nombre": "TV-Cable"},
                    {"nombre": "A/A"},
                    {"nombre": "Espejo"},
                    {"nombre": "Perchero"}
                ]
            },
            {
                "tipo": "Escalera",
                "caracteristicas": [
                    {"nombre": "Granito"},
                    {"nombre": "Marmol"},
                    {"nombre": "Madera"},
                    {"nombre": "Concreto"},
                    {"nombre": "Baranda"},
                    {"nombre": "Calentador"}
                ]
            },
            {
                "tipo": "Piso",
                "caracteristicas": [
                    {"nombre": "Madera"},
                    {"nombre": "Porcelanato"},
                    {"nombre": "Granito"},
                    {"nombre": "Cerámica"},
                    {"nombre": "Cemento"},
                    {"nombre": "Caico"}
                ]
            },
            {
                "tipo": "Seguridad",
                "caracteristicas": [
                    {"nombre": "Cámara"},
                    {"nombre": "DVR"},
                    {"nombre": "Alarma"},
                    {"nombre": "Vigilancia"},
                    {"nombre": "Cerca Elect"},
                    {"nombre": "Monitor"},
                    {"nombre": "B. Pánico"},
                    {"nombre": "Sirena"}
                ]
            },
            {
                "tipo": "Area externa",
                "caracteristicas": [
                    {"nombre": "Patio"},
                    {"nombre": "Piscina"},
                    {"nombre": "Parrillera"},
                    {"nombre": "Jardinera"},
                    {"nombre": "Gimnasio"},
                    {"nombre": "Fuente"},
                    {"nombre": "Tanque de agua"},
                    {"nombre": "Lavandero"},
                    {"nombre": "Reflector"}
                ]
            }
        ]
        '''

        # Cargar JSON
        areas_data = json.loads(areas_json)

        # Guardar en la base de datos
        for area in areas_data:
            tipo_area = area['tipo']
            
            for caracteristica in area['caracteristicas']:
                nombre_caracteristica = caracteristica['nombre']
                Caracteristica.objects.get_or_create(tipo=tipo_area, nombre=nombre_caracteristica)
        
        return redirect('inmueble_detalles', inmueble_id=inmueble_id)

