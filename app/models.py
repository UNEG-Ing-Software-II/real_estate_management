from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
import uuid
import os


AREA_TYPES = [
    ("kitchen", "Cocina"),
    ("living_room", "Sala"),
    ("main_bedroom", "Dormitorio Principal"),
    ("room", "Cuarto"),
    ("stairs", "Escalera"),
    ("floor", "Piso"),
    ("bathroom", "Baño"),
    ("security", "Seguridad"),
    ("external_area", "Area externa"),
]

class CustomUser(BaseUserManager):
    def create_user(self, email, name, last_name, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            email=email, name=name, last_name=last_name, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(*args, **kwargs)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    ROL_CHOICES = [
        ("manager", "Director General"),
        ("coordinator", "Coordinador"),
        ("consultant", "Asesor"),
        ("owner", "Propietario"),
        ("buyer", "Comprador")
    ]

    document = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    image = models.ImageField(null=True)
    role = models.CharField(max_length=20, choices=ROL_CHOICES, default="consultant")
    description = models.CharField(null=True, default="", max_length=200)
    is_admin = models.BooleanField(default=False)
    objects = CustomUser()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "identification_document", "last_name", "role"]

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

    def __str__(self):
        return f"{self.name} {self.last_name} ({self.email})"


class Phone(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)


class Estate(models.Model):
    ESTATE_TYPES = [
        ("apartment", "Apartamento"),
        ("town_house", "Town house"),
        ("country_house", "Quinta"),
        ("house", "Casa"),
        ("shed", "Galpon"),
        ("office", "Oficina"),
        ("f_trade", "F comercio"),
        ("others", "Otros"),
    ]
    STATES = [
        ("sale", "En venta"),
        ("rent", "En alquiler"),
        ("finished", "Finalizado"),
    ]
    name = models.CharField(default="",max_length=30)
    type = models.CharField(max_length=20, choices=ESTATE_TYPES, default="others")
    price = models.FloatField()
    levels = models.IntegerField()
    land_meters = models.FloatField()
    construction_meters = models.FloatField()
    bathroom = models.BooleanField()
    service_room = models.BooleanField()
    office = models.BooleanField()
    parking = models.BooleanField()
    half_bath = models.BooleanField()
    terrace = models.BooleanField()
    room = models.BooleanField()
    trunk = models.BooleanField() # It's something like warehouses, attic, basement ...
    state = models.CharField(max_length=20, choices=STATES, default="sale")
    address = models.CharField(default="", max_length=50)
    latitude = models.FloatField(default=0.0)
    altitude = models.FloatField(default=0.0)

    def create_estate(self, *args, **kwargs):
        estate = Estate(*args, **kwargs)
        estate.save(using=self._db)
        return estate



#FIXME: This can be done with a MANY TO MANY RELATIONSHIP, DJANGO will be in charge of managing the tables
class EstateOwner(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    estate_id = models.ForeignKey(Estate, on_delete=models.CASCADE)


#FIXME: This can be done with a MANY TO MANY RELATIONSHIP, DJANGO will be in charge of managing the tables
class EstateConsultant(models.Model):
    consultant_id = models.ForeignKey(User, on_delete=models.CASCADE)
    estate_id = models.ForeignKey(Estate, on_delete=models.CASCADE)


#TODO: This must be discussed at a general table, even if we do not even do it
class Documents(models.Model):
    consultant_id = models.ForeignKey(User, on_delete=models.CASCADE)
    estate_id = models.ForeignKey(Estate, on_delete=models.CASCADE)
    identification_document = models.BooleanField()
    rif = models.BooleanField()
    property_document = models.BooleanField()
    mortgage_release = models.BooleanField()
    cadastral_record = models.BooleanField()
    municipal_solvency = models.BooleanField()
    housing_principal = models.BooleanField()
    power = models.BooleanField()
    catchment_format = models.BooleanField()
    customer_data = models.BooleanField()
    registry_mega = models.BooleanField()


class Area(models.Model):
    estate_id = models.ForeignKey(Estate, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=AREA_TYPES)


class Feature(models.Model):
    description = models.CharField(max_length=30)
    type = models.CharField(max_length=20, choices=AREA_TYPES)


#FIXME: This is another table of many to many that can be accommodated with a many to many
class AreaFeature(models.Model):
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE)
    feature_id = models.ForeignKey(Feature, on_delete=models.CASCADE)


class Task(models.Model):

    TASK_TYPE = [("catchment", "Captacion"), ("sale", "Venta")]

    name = models.CharField(max_length=200, default="")
    type = models.CharField(max_length=20, choices=TASK_TYPE)
    percentage = models.FloatField()


class EstateTask(models.Model):
    estate_id = models.ForeignKey(Estate, on_delete=models.CASCADE)
    consultant_id = models.ForeignKey(User, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    done = models.BooleanField()



# def get_image_upload_path(instance, filename):
#     # para guardar las imagenes de esta forma>> "inmueble_fotos/<inmueble_id>/<filename>"
#     return os.path.join('inmueble_fotos', str(instance.inmueble.id), filename)

class ImageEstate(models.Model):

    # To save the images in this way>> "estate/<estate>/<filename>"
    def get_image_upload_path(self, filename):
        return os.path.join('estate', str(self.estate_id.id), filename)


    estate_id = models.ForeignKey(Estate, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_upload_path)



class ImageArea(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)  # FK la tabla Area
    image = models.ImageField()

