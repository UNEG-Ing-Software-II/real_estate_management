import os
import sys
import django
import uuid
import json

# Configurar la ruta base del proyecto (un directorio hacia atrás)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyR.settings')
django.setup()

from  app_Principal.models import *

#Scripts para cambiar inmuebles. Ejecutar siempre desde la carpeta scripts
def cargar_inmuebles():
    with open('inmuebles.json', 'r') as inmuebles_json: inmueble_data = json.load(inmuebles_json)
        
    for inmuebles_entrada in inmueble_data: 
        inmueble = Inmueble.objects.create(
            tipoPropiedad=inmuebles_entrada['tipoPropiedad'],
            precio=inmuebles_entrada['precio'],
            niveles=inmuebles_entrada['niveles'],
            metros_terreno=inmuebles_entrada['metros_terreno'],
            metros_construccion=inmuebles_entrada['metros_construccion'],
            bathroom=inmuebles_entrada['bathroom'],
            cuarto_servicio=inmuebles_entrada['cuarto_servicio'],
            oficina=inmuebles_entrada['oficina'],
            estacionamiento=inmuebles_entrada['estacionamiento'],
            half_bath=inmuebles_entrada['half_bath'],
            terraza=inmuebles_entrada['terraza'],
            habitacion=inmuebles_entrada['habitacion'],
            maletero=inmuebles_entrada['maletero'],
            estado=inmuebles_entrada['estado'],
            direccion=inmuebles_entrada['direccion'],
            latitud=inmuebles_entrada['latitud'],
            longitud=inmuebles_entrada['longitud']            
        )
        print(f'Inmueble {inmueble.direccion} creado exitosamente.')

def main():
    cargar_inmuebles()

if __name__ == '__main__':
    main()
