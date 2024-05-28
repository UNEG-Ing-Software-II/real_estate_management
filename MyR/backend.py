from app_Principal.models import *
from django.shortcuts import redirect,render
from app_Principal.models import *
from django.http import request


#esta funcion recibe el rol del usuario que esta logueado, dependiendo lo va a redirigir a su pagina correspondiente
#obviamente va a dar error porque ninguna de las paginas estan predefinidas en el archivo urls.py
#basicamente cada return va llamar a la funcion del archivo views.py que procesa cada vista, claro la direccion debe estar en el archivo urls.py
def redirecion(rol):    
    if rol=='Director General':
        print("usted entro en la vista Director general")
        return redirect('inicio director_General')   
    elif rol=='Coordinador':
        print("usted entro en la vista Coordinador")
        return redirect('inicio Coordinador')
    elif rol=='Asesor':
        print("usted entro en la vista Asesor")
        #return redirect('inicio Asesor')
    elif rol=='Propietario': 
        print("usted entro en la vista Propietario")
        return redirect('inicio Propietario')
    
#funcion temporal para cargar un registro a la tabla usuario




def guardar_usuario():
    usuario = Usuario.objects.create_user(
        cedula='30110259',
        password='password',
        nombre='Pablo',
        apellido='Jimenez',
        rol='Coordinador',
        correo='prjr2002@gmail.com'
    )



  






