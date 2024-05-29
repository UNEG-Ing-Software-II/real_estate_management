from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

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

    objects = UsuarioPersonalizado()

    USERNAME_FIELD = "correo"
    REQUIRED_FIELDS = ["nombre", "apellido", "rol"]

    class Meta:
        db_table = "Usuario"

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.correo})"


class Telefono(models.Model):
    id = models.UUIDField(primary_key=True)
    persona = models.ForeignKey(
        Usuario, on_delete=models.CASCADE
    )  # FK la tabla Usuario
    telefono = models.CharField(
        max_length=15
    )  # numero de contacto, tipo char porque puede tener +58 y asi

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
    id = models.UUIDField(primary_key=True)
    propietario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE
    )  # FK la tabla Usuario
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
    maletero = models.BooleanField()  # es algo como almacenes aticos, sotano...

    class Meta:
        db_table = "Inmueble"


class Documentos(models.Model):  # documentos del inmueble
    id = models.UUIDField(primary_key=True)
    asesor = models.ForeignKey(
        Usuario, on_delete=models.CASCADE
    )  # FK la tabla Usuario
    inmueble = models.ForeignKey(
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
    id = models.UUIDField(primary_key=True)
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
    id = models.UUIDField(primary_key=True)
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
    id = models.UUIDField(primary_key=True)
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
    id = models.UUIDField(primary_key=True)
    inmueble = models.ForeignKey(
        Inmueble, on_delete=models.CASCADE
    )  # FK la tabla Inmueble
    asesor = models.ForeignKey(
        Usuario, on_delete=models.CASCADE
    )  # FK la tabla Usuario
    tipo = models.CharField(
        max_length=20,
        choices=TIPO_INCIDENCIA_CHOICES,
    )
    realizado = models.BooleanField()
    porcentaje = models.FloatField()

    class Meta:
        db_table = "Incidencia"


class Imagen_inmueble(models.Model):
    id = models.UUIDField(primary_key=True)
    inmueble = models.ForeignKey(
        Inmueble, on_delete=models.CASCADE
    )  # FK la tabla Inmueble
    foto = models.ImageField()

    class Meta:
        db_table = "imagen_inmueble"


class Imagen_area(models.Model):
    id = models.UUIDField(primary_key=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)  # FK la tabla Area
    foto = models.ImageField()

    class Meta:
        db_table = "imagen_area"
