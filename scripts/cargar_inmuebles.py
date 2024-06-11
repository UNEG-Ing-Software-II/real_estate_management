from populate_db import configure_env
import json

configure_env()

from  app_Principal.models import *


data = open("inmuebles.json").read()
create_data = Inmueble.objects.create

for inmuebles_entrada in json.loads(data):
    inmueble = create_data(**inmuebles_entrada)
    print("Inmueble %s creado exitosamente." %inmueble.direccion)

