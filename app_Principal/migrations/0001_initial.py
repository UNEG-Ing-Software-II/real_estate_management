# Generated by Django 5.0.6 on 2024-06-16 23:38

import app_Principal.models
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('cedula', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('foto', models.ImageField(null=True, upload_to='')),
                ('rol', models.CharField(choices=[('Director General', 'Director General'), ('Coordinador', 'Coordinador'), ('Asesor', 'Asesor'), ('Propietario', 'Propietario')], default='Asesor', max_length=20)),
                ('descripcion', models.CharField(default='', max_length=200, null=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Usuario',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('Cocina', 'Cocina'), ('Sala', 'Sala'), ('Dormitorio Principal', 'Dormitorio Principal'), ('Cuarto', 'Cuarto'), ('Escalera', 'Escalera'), ('Piso', 'Piso'), ('Baño', 'Baño'), ('Seguridad', 'Seguridad'), ('Area externa', 'Area externa')], max_length=20)),
            ],
            options={
                'db_table': 'Area',
            },
        ),
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('Cocina', 'Cocina'), ('Sala', 'Sala'), ('Dormitorio Principal', 'Dormitorio Principal'), ('Cuarto', 'Cuarto'), ('Escalera', 'Escalera'), ('Piso', 'Piso'), ('Baño', 'Baño'), ('Seguridad', 'Seguridad'), ('Area externa', 'Area externa')], max_length=20)),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Caracteristica',
            },
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tipoPropiedad', models.CharField(choices=[('Apartamento', 'Apartamento'), ('Town house', 'Town house'), ('Quinta', 'Quinta'), ('Casa', 'Casa'), ('Galpon', 'Galpon'), ('Oficina', 'Oficina'), ('F comercio', 'F comercio'), ('Otros', 'Otros')], default='Otros', max_length=20)),
                ('nombre', models.CharField(default='', max_length=30)),
                ('precio', models.FloatField()),
                ('niveles', models.IntegerField()),
                ('metros_terreno', models.FloatField()),
                ('metros_construccion', models.FloatField()),
                ('bathroom', models.BooleanField()),
                ('cuarto_servicio', models.BooleanField()),
                ('oficina', models.BooleanField()),
                ('estacionamiento', models.BooleanField()),
                ('half_bath', models.BooleanField()),
                ('terraza', models.BooleanField()),
                ('habitacion', models.BooleanField()),
                ('maletero', models.BooleanField()),
                ('estado', models.CharField(choices=[('En venta', 'En venta'), ('En alquiler', 'En alquiler'), ('Finalizado', 'Finalizado')], default='En venta', max_length=20)),
                ('direccion', models.CharField(default='', max_length=50)),
                ('latitud', models.FloatField(default=0.0)),
                ('longitud', models.FloatField(default=0.0)),
            ],
            options={
                'db_table': 'Inmueble',
            },
        ),
        migrations.CreateModel(
            name='Area_caracteristicas',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Principal.area')),
                ('caracteristica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Principal.caracteristica')),
            ],
            options={
                'db_table': 'Area_caracterisiticas',
            },
        ),
        migrations.CreateModel(
            name='Imagen_area',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('foto', models.ImageField(upload_to='')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Principal.area')),
            ],
            options={
                'db_table': 'imagen_area',
            },
        ),
        migrations.CreateModel(
            name='Incidencia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='', max_length=50)),
                ('tipo', models.CharField(choices=[('Captacion', 'Captacion'), ('Venta', 'Venta')], max_length=20)),
                ('realizado', models.BooleanField()),
                ('porcentaje', models.FloatField()),
                ('asesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Principal.inmueble')),
            ],
            options={
                'db_table': 'Incidencia',
            },
        ),
        migrations.CreateModel(
            name='Imagen_inmueble',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('foto', models.ImageField(upload_to=app_Principal.models.get_image_upload_path)),
                ('inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Principal.inmueble')),
            ],
            options={
                'db_table': 'imagen_inmueble',
            },
        ),
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cedula', models.BooleanField()),
                ('rif', models.BooleanField()),
                ('documento_propiedad', models.BooleanField()),
                ('liberacion_hipoteca', models.BooleanField()),
                ('ficha_catastral', models.BooleanField()),
                ('solvencia_municipal', models.BooleanField()),
                ('vivienda_principal', models.BooleanField()),
                ('poder', models.BooleanField()),
                ('formato_captacion', models.BooleanField()),
                ('datos_cliente', models.BooleanField()),
                ('registro_mega', models.BooleanField()),
                ('asesor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('inmueble_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Principal.inmueble')),
            ],
            options={
                'db_table': 'Documentos',
            },
        ),
        migrations.AddField(
            model_name='area',
            name='inmueble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Principal.inmueble'),
        ),
        migrations.CreateModel(
            name='InmuebleAsesor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('inmueble_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Principal.inmueble')),
                ('persona_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'InmuebleAsesor',
            },
        ),
        migrations.CreateModel(
            name='InmueblePropietario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('inmueble_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Principal.inmueble')),
                ('persona_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'InmueblePropietario',
            },
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('telefono', models.CharField(max_length=15)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Telefono',
            },
        ),
    ]
