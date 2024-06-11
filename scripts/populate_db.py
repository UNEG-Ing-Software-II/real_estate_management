import os
import sys
import django


def configure_env():
    # Configurar la ruta base del proyecto (un directorio hacia atrás)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(BASE_DIR)

    # Configurar el entorno de Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyR.settings')
    django.setup()
