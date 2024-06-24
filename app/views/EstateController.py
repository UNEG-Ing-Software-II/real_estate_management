# forms.py
import shutil
from django import forms
from app.models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from MyR.backend import role_required
from collections import defaultdict
import json

class EstateForm(forms.ModelForm):
    class Meta:
        model = Estate
        fields = "__all__"


class EstateController:

    @login_required(login_url="login")
    def create(request):
        if request.method == "POST":
            form = EstateForm(request.POST)
            if form.is_valid():
                form.save()
        return redirect("home")


    login_required(login_url="login")
    def read(request, estate_id):
        res = defaultdict()
        estate = get_object_or_404(Estate, id=estate_id)
        res["template_name"] = "estate_form.html"
        res["context"] = {
            "estate": estate,
            "estate_images": ImageEstate.objects.filter(estate_id=estate_id),
            "tasks": Task.objects.all(),
            "estate_tasks": EstateTask.objects.filter(estate_id=estate_id),
            "consultants": User.objects.filter(role="consultant"),
            "owners": EstateOwner.objects.filter(estate_id=estate_id),
            "features": Feature.objects.all().order_by("type", "description"),
            "areas": Area.objects.filter(estate_id=estate_id),
            "area_types_set": {item[0]: item[1] for item in AREA_TYPES}
            # "area_types_set": set(Feature.objects.values_list("type", flat=True))
        }

        return render(request, **res)
    
    @login_required(login_url="login")
    def search(request):
        query = request.GET.get('q')
        results = Estate.objects.filter(name__icontains=query) if query else None
        return render(request, 'estate_search.html', {'estates': results, 'query': query})

    @login_required(login_url="login")
    def update(request):

        estate = get_object_or_404(Estate, id=request.POST.get("estate_id"))

        if request.method != "POST":
            return redirect("home")

        form = EstateForm(request.POST, instance=estate)

        if form.is_valid():
            form.save()

            for image in request.FILES.getlist("images"):
                ImageEstate.objects.create(estate_id=estate, image=image)

            if request.POST.get("deletedImages"):
                for image_id in json.loads(request.POST.get("deletedImages")):
                    try:
                        image_estate = ImageEstate.objects.get(id=image_id)

                        if image_estate.image and os.path.isfile(image_estate.image.path):
                            os.remove(image_estate.image.path)

                        image_estate.delete()
                    except ImageEstate.DoesNotExist:
                        continue
        return redirect("estate", estate_id=estate.id)


    def delete(request):
        estate = get_object_or_404(Estate, id=request.POST["estate_id"])

        if request.method != "POST":
            return redirect("home")

        images = ImageEstate.objects.filter(estate_id=estate)
        if images.exists():
            image_path = os.path.dirname(images.first().image.path)
            if os.path.isdir(image_path):
                shutil.rmtree(image_path)
        images.delete()
        estate.delete()
        return redirect("home")



























# @login_required(login_url='login')
# @role_required('Asesor')
# def eliminar_inmueble(request, inmueble_id):
#     # Obtener el inmueble por su ID
#     inmueble = get_object_or_404(Inmueble, id=inmueble_id)
#     if request.method == 'POST':
#         imagenes = Imagen_inmueble.objects.filter(inmueble=inmueble)
#         if imagenes.exists():
#             image_path = os.path.dirname(imagenes.first().foto.path)
#             if os.path.isdir(image_path):
#                 shutil.rmtree(image_path)
#         imagenes.delete()
#         inmueble.delete()
#         return redirect('inicio Asesor')
#     return redirect('inicio Asesor')


# views.py
# @login_required(login_url='login')
# @role_required('Asesor')
# def registrar_inmueble(request):
#     if request.method == 'POST':
#         form = InmuebleForm(request.POST)
#         if form.is_valid():
#             form.save()
            

#             return redirect('inicio Asesor')
#     return redirect('inicio Asesor')


# @login_required(login_url='login')
# @role_required('Asesor')
# def modificar_inmueble(request, inmueble_id):
#     # Obtener el inmueble por su ID
#     inmueble = get_object_or_404(Inmueble, id=inmueble_id)
#     if request.method == 'POST':
#         form = InmuebleForm(request.POST, instance=inmueble)
#         if form.is_valid():
#             form.save()
#             #Nuevas Imagenes
#             fotos = request.FILES.getlist('fotos')
#             for foto in fotos:
#                 imagen_inmueble = Imagen_inmueble()
#                 imagen_inmueble.inmueble = inmueble
#                 imagen_inmueble.foto = foto
#                 imagen_inmueble.save()
            
#             #Imágenes eliminadas
#             deleted_images = request.POST.get('deletedImages')
#             if deleted_images:
#                 deleted_images = json.loads(deleted_images)
#                 for image_id in deleted_images:
#                     try:
#                         image = Imagen_inmueble.objects.get(id=image_id)
                        
#                         if image.foto and os.path.isfile(image.foto.path):
#                             os.remove(image.foto.path)
                        
#                         image.delete()
#                     except Imagen_inmueble.DoesNotExist:
#                         continue
#             return redirect('inicio Asesor')
#     return redirect('inicio Asesor')