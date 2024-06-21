from django.shortcuts import render, get_object_or_404, render, redirect
from django.http import JsonResponse
from app.models import *
from django.views.decorators.csrf import csrf_exempt
import json


class UserController:

    @csrf_exempt
    def save_owner(request):
        if request.method != 'POST':
            return JsonResponse({"error": "Method not allowed"}, status=405)

        owner = None
        method = request.POST.get('method')
        owner_data = {
            "document": request.POST.get('document'),
            "name": request.POST.get('name'),
            "last_name": request.POST.get('last_name'),
            "email": request.POST.get('email'),
            "password": request.POST.get('password', None),
            "role": "owner"
        }

        if method == "new":
            owner = User.objects.create_user(**owner_data)

        if method == "existing":
            owner = get_object_or_404(User, document=owner_data["document"], role="owner")

        estate = get_object_or_404(Estate, id=request.POST.get('estate_id'))
        EstateOwner.objects.create(owner_id=owner, estate_id=estate)
        return redirect("home")


    def unlink_owner(request):
        if request.method != "POST":
            return JsonResponse({"error": "Method not allowed"}, status=405)

        for relation in request.POST.getlist("selected_owners"):
            EstateOwner.objects.filter(id=relation).delete()

        return redirect("home")


    def search_owner(request):
        owner = User.objects.filter(document=request.GET.get("document", role="owner").first())
        estate = Estate.objects.filter(id=request.GET.get("estate_id"))

        if request != "GET":
            return JsonResponse({"error": "Not proportionate card"}, status=400)

        if not owner:
            return JsonResponse({"error": "Owner not found"}, status=400)

        owner_data = {
            "name": owner.name,
            "document": owner.document,
            "last_name": owner.last_name,
            "email": owner.email,
            "msg": "This owner already has this property ",
            "valid": False
        }

        if  not EstateOwner.objects.filter(owner_id=owner, estate=estate).exists():
            owner_data.update({"valid": False})

        return JsonResponse(owner_data, 200)


    def validate_owner(request):
        if request.method != "POST":
            return JsonResponse({"error": "Method not allowed."}, status=405)

        filter_by = User.objects.filter
        document= request.POST.get("document")
        email =  request.POST.get("email")

        if filter_by(document=document).exists() or filter_by(email=email).exists():
            return JsonResponse({"error": "The card or mail is already in use."}, status=400)

        # Return a successful response in JSON format
        return JsonResponse({"success": "Successful validation."})



    # def buscar_propietario(request):
    #     if request.method == 'GET':
    #         cedula = request.GET.get('cedula', None)
    #         inmueble_id = request.GET.get('id_inmueble', None)
    #         inmueble = Inmueble.objects.get(id=inmueble_id)
    #         if cedula:
    #             propietario = Usuario.objects.filter(cedula=cedula, rol="Propietario").first()
    #             if propietario:
    #                 if InmueblePropietario.objects.filter(persona_id=propietario, inmueble_id=inmueble).exists():
    #                     return JsonResponse({
    #                         'cedula': propietario.cedula,
    #                         'nombre': propietario.nombre,
    #                         'apellido': propietario.apellido,
    #                         'correo': propietario.correo,
    #                         'msg': 'Este propietario ya posee este inmueble',
    #                         'valido':False,
    #                     }, status=200)
    #                 else:
    #                     return JsonResponse({
    #                         'cedula': propietario.cedula,
    #                         'nombre': propietario.nombre,
    #                         'apellido': propietario.apellido,
    #                         'correo': propietario.correo,
    #                         'valido':True,
    #                     }, status=200)
    #             else:
    #                 return JsonResponse({'error': 'Propietario no encontrado'}, status=404)
    #         else:
    #             return JsonResponse({'error': 'Cédula no proporcionada'}, status=400)

    # @csrf_exempt
    # def validar_propietario(request):
    #     if request.method == 'POST':
    #         cedula = request.POST.get('cedula')
    #         correo = request.POST.get('correo')

    #         if Usuario.objects.filter(cedula=cedula).exists():
    #             return JsonResponse({'error': 'La cédula ya está en uso.'}, status=400)

    #         if Usuario.objects.filter(correo=correo).exists():
    #             return JsonResponse({'error': 'El correo ya está en uso.'}, status=400)

    #         # Retornar una respuesta exitosa en formato JSON
    #         return JsonResponse({'success': 'Validación exitosa.'})

    #     return JsonResponse({'error': 'Método no permitido.'}, status=405)
        


    # @csrf_exempt
    # def guardar_propietario_inmueble(request):
    #     if request.method == 'POST':
    #         cedula = request.POST.get('cedula')
    #         nombre = request.POST.get('nombre')
    #         apellido = request.POST.get('apellido')
    #         correo = request.POST.get('correo')
    #         password = request.POST.get('password', None)
    #         method = request.POST.get('method')

    #         if method == 'nuevo':
    #             # Crear un nuevo propietario
    #             propietario = Usuario.objects.create_user(
    #                 correo=correo,
    #                 nombre=nombre,
    #                 apellido=apellido,
    #                 password=password,
    #                 cedula=cedula,
    #                 rol="Propietario"
    #             )
    #         elif method == 'existente':
    #             propietario = get_object_or_404(Usuario, cedula=cedula, rol="Propietario")

    #         # Obtener el inmueble y crear la relación
    #         inmueble = get_object_or_404(Inmueble, id=request.POST.get('inmueble_id'))
    #         InmueblePropietario.objects.create(persona_id=propietario, inmueble_id=inmueble)

    #         return redirect('inicio Asesor')

    #     return JsonResponse({'error': 'Método no permitido'}, status=405)
