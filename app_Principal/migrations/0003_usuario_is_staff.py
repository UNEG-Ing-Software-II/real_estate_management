# Generated by Django 5.0.6 on 2024-05-29 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Principal', '0002_usuario_foto_imagen_area_imagen_inmueble'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
