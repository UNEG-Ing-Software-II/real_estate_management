from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
import uuid
import os


TIPO_AREA_CHOICES = [
    ("Cocina", "Cocina"),
    ("Sala", "Sala"),
    ("Dormitorio Principal", "Dormitorio Principal"),
    ("Cuarto", "Cuarto"),
    ("Escalera", "Escalera"),
    ("Piso", "Piso"),
    ("Baño", "Baño"),
    ("Seguridad", "Seguridad"),
    ("Area externa", "Area externa"),
]


class UsuarioPersonalizado(BaseUserManager):
    def create_user(self, correo, nombre, apellido, password, **extra_fields):
        correo = self.normalize_email(correo)
        user = self.model(
            correo=correo, nombre=nombre, apellido=apellido, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(*args, **kwargs)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    ROL_CHOICES = [
        ("Director General", "Director General"),
        ("Coordinador", "Coordinador"),
        ("Asesor", "Asesor"),
        ("Propietario", "Propietario"),
    ]
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField(unique=True)
    foto = models.ImageField(null=True)
    rol = models.CharField(
        max_length=20,
        choices=ROL_CHOICES,
        default="Asesor",
    )
    descripcion = models.CharField(null=True)
    is_admin = models.BooleanField(default=False)
    objects = UsuarioPersonalizado()

    USERNAME_FIELD = "correo"
    REQUIRED_FIELDS = ["nombre", "cedula", "apellido", "rol"]

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        db_table = "Usuario"

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.correo})"


class Telefono(models.Model):
    id = models.UUIDField(primary_key=True)
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)

    class Meta:
        db_table = "Telefono"


class Inmueble(models.Model):
    PROPIEDAD_CHOICES = [
        ("Apartamento", "Apartamento"),
        ("Town house", "Town house"),
        ("Quinta", "Quinta"),
        ("Casa", "Casa"),
        ("Galpon", "Galpon"),
        ("Oficina", "Oficina"),
        ("F comercio", "F comercio"),
        ("Otros", "Otros"),
    ]
    ESTADO_CHOICES = [
        ("En venta", "En venta"),
        ("En alquiler", "En alquiler"),
        ("Finalizado", "Finalizado"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipoPropiedad = models.CharField(
        max_length=20,
        choices=PROPIEDAD_CHOICES,
        default="Otros",
    )
    precio = models.FloatField()
    niveles = models.IntegerField()
    metros_terreno = models.FloatField()
    metros_construccion = models.FloatField()
    bathroom = models.BooleanField()
    cuarto_servicio = models.BooleanField()
    oficina = models.BooleanField()
    estacionamiento = models.BooleanField()
    half_bath = models.BooleanField()  # medio baño
    terraza = models.BooleanField()
    habitacion = models.BooleanField()
    maletero = (
        models.BooleanField()
    )  # es algo como almacenes, áticos, sotano...
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default="En venta",
    )
    direccion = models.CharField(default=" ")
    latitud = models.FloatField(default=0.0)
    longitud = models.FloatField(default=0.0)

    def create_inmueble(self, tipoPropiedad, precio, niveles,
                        metros_terreno, metros_construccion, 
                        bathroom, cuarto_servicio, oficina, 
                        estacionamiento, half_bath, terraza, 
                        habitacion, maletero, estado, direccion, 
                        latitud, longitud):
        inmueble = Inmueble(
            tipoPropiedad=tipoPropiedad,
            precio=precio,
            niveles=niveles,
            metros_terreno=metros_terreno,
            metros_construccion=metros_construccion,
            bathroom=bathroom,
            cuarto_servicio=cuarto_servicio,
            oficina=oficina,
            estacionamiento=estacionamiento,
            half_bath=half_bath,
            terraza=terraza,
            habitacion=habitacion,
            maletero=maletero,
            estado=estado,
            direccion=direccion,
            latitud=latitud,
            longitud=longitud
        )
        inmueble.save(using=self._db)
        return inmueble

    class Meta:
        db_table = "Inmueble"


class InmueblePropietario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    persona_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    inmueble_id = models.ForeignKey(Inmueble, on_delete=models.CASCADE)

    class Meta:
        db_table = "InmueblePropietario"

class InmuebleAsesor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    persona_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    inmueble_id = models.ForeignKey(Inmueble, on_delete=models.CASCADE)

    class Meta:
        db_table = "InmuebleAsesor"


class Documentos(models.Model):  # documentos del inmueble
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asesor_id = models.ForeignKey(
        Usuario, on_delete=models.CASCADE
    )  # FK la tabla Usuario
    inmueble_id = models.ForeignKey(
        Inmueble, on_delete=models.CASCADE
    )  # FK la tabla Inmueble
    cedula = models.BooleanField()
    rif = models.BooleanField()
    documento_propiedad = models.BooleanField()
    liberacion_hipoteca = models.BooleanField()
    ficha_catastral = models.BooleanField()
    solvencia_municipal = models.BooleanField()
    vivienda_principal = models.BooleanField()  # registro de vivienda principal
    poder = models.BooleanField()  # npi que es poder
    formato_captacion = models.BooleanField()
    datos_cliente = models.BooleanField()
    registro_mega = models.BooleanField()  # escaneado y guardado en mega

    class Meta:
        db_table = "Documentos"


class Area(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inmueble = models.ForeignKey(
        Inmueble, on_delete=models.CASCADE
    )  # FK la tabla Inmueble
    tipo = (
        models.CharField(  # seleccion de tipo de area, definido en la linea 3
            max_length=20,
            choices=TIPO_AREA_CHOICES,
        )
    )

    class Meta:
        db_table = "Area"


class Caracteristica(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = (
        models.CharField(  # seleccion de tipo de area, definido en la linea 3
            max_length=20,
            choices=TIPO_AREA_CHOICES,
        )
    )
    nombre = models.CharField(max_length=20)

    class Meta:
        db_table = "Caracteristica"


class Area_caracteristicas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)  # FK la tabla Area
    caracteristica = models.ForeignKey(
        Caracteristica, on_delete=models.CASCADE
    )  # FK la tabla Area

    class Meta:
        db_table = "Area_caracterisiticas"


class Incidencia(models.Model):
    TIPO_INCIDENCIA_CHOICES = [
        ("Captacion", "Captacion"),
        ("Venta", "Venta"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inmueble = models.ForeignKey(
        Inmueble, on_delete=models.CASCADE
    )  # FK la tabla Inmueble
    asesor = models.ForeignKey(
        Usuario, on_delete=models.CASCADE
    )  # FK la tabla Usuario
    nombre = models.CharField(
        max_length=50,
        default="",
    )
    tipo = models.CharField(
        max_length=20,
        choices=TIPO_INCIDENCIA_CHOICES,
    )
    realizado = models.BooleanField()
    porcentaje = models.FloatField()

    class Meta:
        db_table = "Incidencia"

def get_image_upload_path(instance, filename):
    # para guardar las imagenes de esta forma>> "inmueble_fotos/<inmueble_id>/<filename>"
    return os.path.join('inmueble_fotos', str(instance.inmueble.id), filename)

class Imagen_inmueble(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inmueble = models.ForeignKey(
        Inmueble, on_delete=models.CASCADE
    )  # FK la tabla Inmueble
    foto = models.ImageField(upload_to=get_image_upload_path)

    class Meta:
        db_table = "imagen_inmueble"


class Imagen_area(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)  # FK la tabla Area
    foto = models.ImageField()

    class Meta:
        db_table = "imagen_area"
