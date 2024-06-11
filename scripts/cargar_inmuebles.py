from populate_db import configure_env
import json

configure_env()

from  app_Principal.models import *


for inmuebles_entrada in json.loads(open("inmuebles.json").read()):
    inmueble = Inmueble.objects.create(**inmuebles_entrada)
    print("Inmueble %s creado exitosamente." %inmueble.direccion)

