
from django.shortcuts import render, redirect
from app_Principal.models import *
from django.http import request
from MyR.backend import * #importancion para funciones de la carpeta backend.py
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages #importacion para mensajes de error
from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

#funcion para procesar el inicio de sesion
def index(request):
    if request.user.is_authenticated: #verificamos primero si en el computador  hay un usario logueado
        messages.error(request, 'usted ya esta logueado.', extra_tags='access_denied')
        User = request.user
        return redirecion(User.rol)  # llama a la funcion redirecion que se encuentra en el archivo backend.py y determina su inicio dependiendo el rol
   
    next_page = request.GET.get('next')

    if request.method == "POST": #si el usuario no esta logueado, se recibe las credenciales y se procesan
        correo = request.POST["correo"]
        password = request.POST["password"]
        user = authenticate(correo=correo, password=password)

        if user is not None:
            login(request, user)
            print("usuario: ",user)

            if next_page:
                return redirect(next_page)  # Redirigir al usuario a la página 'next' después de iniciar sesión (osea la pagina que intento visitar antes)
            else:
                return redirecion(user.rol)  # llama a la funcion redirecion que se encuentra en el archivo backend.py y determina su inicio dependiendo el rol
        else:
            guardar_usuario()
            error_message = 'Credenciales inválidas. Por favor, inténtalo de nuevo.'
            return render(request, 'index.html', {'error_message': error_message}) #vuelva a llamar al inicio de login y manda el mensaje de error

    return render(request, 'index.html', {'next_page': next_page})

def coordinador(request):
   
    return render(request,'inicio_coordinador.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('index')


#-------------------------------------------------------------------------------------#
#CRUD para los inmuebles


#Leer inmuebles
def read_inmueble(request):
  if request.method == 'GET':
      # Consulta a la tabla Inmueble para obtener todos los registros
      inmueble = Inmueble.objects.all()

      # Pasar los datos al contexto de renderizado
      context = {'inmuebles': inmueble}

      return render(request,'read_inmueble.html',context)


#Crear inmueble
def create_inmueble(request):
  if request.method == 'GET':

    usuario = Usuario.objects.all()
    context = {'usuario': usuario}
    return render(request, 'create_inmueble.html', context)
  else:
    propietario_id = request.POST['propietario_id']
    precio = request.POST['precio']
    tipoPropiedad =  request.POST['tipoPropiedad']
    niveles =  request.POST['niveles']
    metros_terreno = request.POST['metros_terreno']
    metros_construccion = request.POST['metros_construccion']
    bathroom = request.POST['bathroom']
    cuarto_servicio = request.POST['cuarto_servicio']
    oficina = request.POST['oficina']
    estacionamiento = request.POST['estacionamiento']
    half_bath = request.POST['half_bath']
    terraza = request.POST['terraza']
    habitacion = request.POST['habitacion']
    maletero = request.POST['maletero']
    



    Inmueble.objects.create(propietario_id = propietario_id , precio = precio, tipoPropiedad = tipoPropiedad, 
                            niveles = niveles, metros_terreno = metros_terreno, metros_construccion = metros_construccion,
                            bathroom = bathroom, cuarto_servicio = cuarto_servicio, oficina = oficina, estacionamiento = estacionamiento,
                            half_bath = half_bath, terraza = terraza, habitacion = habitacion, maletero = maletero)
    
    return redirect('/view_director_g/create_inmueble')
  


#Modificar inmueble
  
def update_inmueble(request):
  if request.method == 'GET':
    inmueble = Inmueble.objects.all()
    usuario = Usuario.objects.all()
    context ={'inmuebles': inmueble, 'usuario':usuario}
    return render(request,'update_inmueble.html',context)
  else:

        # Obtener los datos actualizados del formulario
        inmueble_id = request.POST['inmueble']
        propietario_id = request.POST['propietario_id']
        precio = request.POST['precio']
        tipoPropiedad =  request.POST['tipoPropiedad']
        niveles =  request.POST['niveles']
        metros_terreno = request.POST['metros_terreno']
        metros_construccion = request.POST['metros_construccion']
        bathroom = request.POST['bathroom']
        cuarto_servicio = request.POST['cuarto_servicio']
        oficina = request.POST['oficina']
        estacionamiento = request.POST['estacionamiento']
        half_bath = request.POST['half_bath']
        terraza = request.POST['terraza']
        habitacion = request.POST['habitacion']
        maletero = request.POST['maletero']
        

        inmueble = get_object_or_404(Inmueble, pk=inmueble_id)
        
        # Actualizar los campos del inmueble
        inmueble.propietario_id = propietario_id
        inmueble.precio = precio
        inmueble.tipoPropiedad = tipoPropiedad
        inmueble.niveles = niveles
        inmueble.metros_terreno = metros_terreno
        inmueble.metros_contruccion = metros_construccion
        inmueble.bathroom = bathroom
        inmueble.cuarto_servicio = cuarto_servicio
        inmueble.oficina = oficina
        inmueble.estacionamiento = estacionamiento
        inmueble.half_bath = half_bath
        inmueble.terraza = terraza
        inmueble.habitacion = habitacion
        inmueble.maletero = maletero



        # Guardar los cambios en la base de datos
        inmueble.save()
        return redirect('/view_director_g/update_inmueble/')


def delete_inmueble(request):
  if request.method == 'GET':
      inmueble = Inmueble.objects.all()
      # Pasar los datos al contexto de renderizado
      context = {'inmueble': inmueble}
      return render(request, 'delete_edificio.html', context)
  else:
     inmueble_id = request.POST['inmueble']
     inmueble = get_object_or_404(Inmueble, pk=inmueble_id)
      # Eliminar el condominio
     inmueble.delete()
     return redirect('/view_director_g/delete_inmueble/')
  

