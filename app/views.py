from django.shortcuts import render, redirect
from app.models import *
from django.http import request
from MyR.backend import *  # Import for functions of the backend.py folder
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Import for error messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.contrib.auth import update_session_auth_hash
from collections import defaultdict

# Create your views here.
@login_required(login_url="login")
def home(request):
    res = defaultdict()

    if request.user.role == "manager":
        res["template_name"] = "inicio_DG.html"

    if request.user.role == "coordinator":
        res["template_name"] = "inicio_coordinador.html"

    if request.user.role == "consultant":
        res["template_name"] = "views_asesor.html"
        res["context"] = {
            "estates": [{
                "estate": estate,
                "owners": EstateOwner.objects \
                    .filter(estate_id=estate.id) \
                    .select_related("owner_id")
            } for estate in Estate.objects.all()]
        }

        return render(request, **res)


def sign_in(request):
    if request.user.is_authenticated:
        return redirect("home")

    if not request.method == "POST":
        context = {"next_page": request.GET.get("next_page")}
        return render(request, "login.html", context)

    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(email=username, password=password)

    if user is None:
        template = "login.html",
        context = {"error_message": "Wrong User/Password"}
        return render(request, template, context)

    login(request, user)
    next_page = request.GET.get("next_page", "home")
    return redirect(next_page)


def sign_off(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def my_account(request):

    def _validate_unique(user, value):
        return User.objects.exclude(pk=user.pk).filter(**value).exists()


    if request.method != "POST":
        return render(request, 'datos_cuenta.html', {'user': request.user})

    user = request.user
    POST = request.POST

    if POST["document"]:

        if _validate_unique(user, {"document": POST["document"]}):
            messages.error(request, "This document is already in use")
            return redirect("my_account")

        user.document = POST["document"]

    if POST["email"]:

        if _validate_unique(user, {"email": POST["email"]}):
            messages.error(request, "This e-mail is already in use")
            return redirect("my_account")

        user.email = POST["email"]

    if POST.get("password"):
        user.set_password(POST.get("password"))

    user.name = POST.get("name", user.name)
    user.last_name = POST.get("last_name", user.last_name)

    user.save()
    messages.success(request, "Updated data correctly")
    return redirect("my_account")


def sign_up(request):
    if request.method != "POST":
        return render(request,"sign_up.html")

    user_data = {
        "name": request.POST["name"],
        "last_name": request.POST["last_name"],
        "document": request.POST["document"],
        "email": request.POST["email"],
        "role": request.POST["role"],
        "password": request.POST["password"],
    }

    User.objects.create_user(**user_data)
    return render(request, "index.html")



# # ESTO BORRA TODAS LAS TABLAS DEL RAILWAY Y LOCAL, USAR CUANDO SE ACTUALICE LA BD
# from django.db import connection

# def eliminar_todas_las_tablas():
#     with connection.cursor() as cursor:

#         cursor.execute('SET session_replication_role = replica;')
#         cursor.execute('DROP SCHEMA public CASCADE; CREATE SCHEMA public;')
#         cursor.execute('SET session_replication_role = DEFAULT;')

#     print("Todas las tablas han sido eliminadas, incluyendo aquellas con restricciones de clave externa.")

# eliminar_todas_las_tablas()
