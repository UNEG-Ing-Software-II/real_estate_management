import os
import sys
import django
import json

# Configurar la ruta base del proyecto (un directorio hacia atrás)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Configurar el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyR.settings")
django.setup()

from app_Principal import models

ARGS = [
    {
        "key": "estate",
        "file": "inmuebles.json",
        "model": models.Inmueble,
    },
    {
        "key": "users",
        "file": "usuarios.json",
        "model": models.Usuario,
        "function": models.Usuario.objects.create_user,
    },
]

if len(sys.argv) > 1:
    ARGS = [*filter(lambda arg: arg["key"] in sys.argv, ARGS)]

for item in ARGS:
    data = json.loads(open(item["file"]).read())
    for registry in data:
        try:
            model = (
                item["function"](**registry)
                if item.get("function")
                else item["model"].objects.create(**registry)
            )
            print(
                "%s (%s) Created satisfactorily"
                % (model.nombre, item["key"].upper())
            )
        except:
            pass
