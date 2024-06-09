import os
import sys
import django
import uuid
import json

###### comando: Python scripts/usuarios_script.py create_users #######

# Configurar la ruta base del proyecto (un directorio hacia atrás)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyR.settings')
django.setup()

from  app_Principal.models import *

def create_users(json_file_path):
    
    with open(json_file_path, 'r') as json_file:
        users_data = json.load(json_file)

    
    for user_data in users_data:
        user = Usuario.objects.create_user(
            cedula=user_data['cedula'],
            nombre=user_data['nombre'],
            apellido=user_data['apellido'],
            correo=user_data['correo'],
            rol=user_data['rol'],
            password=user_data['password']
        )
        print(f'Usuario {user.nombre} {user.apellido} creado exitosamente.')

def main():
    json_file_path = 'scripts/usuarios.json' 
    create_users(json_file_path)

if __name__ == '__main__':
    main()
