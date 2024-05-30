import os
import sys
import django
import uuid

# Configurar la ruta base del proyecto (un directorio hacia atrás)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyR.settings')
django.setup()

from  app_Principal.models import *

def create_users():
    users_data = [
        {
            'cedula': 1,
            'nombre': 'Juan',
            'apellido': 'Pérez',
            'correo': 'juan.perez@example.com',
            'password': 'password123',
            'rol': 'Asesor'
        },
        {
            'cedula': 2,
            'nombre': 'Ana',
            'apellido': 'Gómez',
            'correo': 'ana.gomez@example.com',
            'password': 'password123',
            'rol': 'Coordinador'
        },
        {
            'cedula': 3,
            'nombre': 'Luis',
            'apellido': 'Martínez',
            'correo': 'luis.martinez@example.com',
            'password': 'password123',
            'rol': 'Director General'
        }
    ]

    for user_data in users_data:
        user = Usuario.objects.create_user(
            cedula=user_data['cedula'],
            correo=user_data['correo'],
            nombre=user_data['nombre'],
            apellido=user_data['apellido'],
            password=user_data['password'],
            rol=user_data['rol']
        )
        user.save()
        print(f'Usuario {user.nombre} {user.apellido} creado exitosamente.')

def main():
    create_users()

if __name__ == '__main__':
    main()
