# Generated by Django 4.1.2 on 2022-11-09 22:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_extesionusuari2'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExtesionUsuari2',
            new_name='ExtesionUsuario2',
        ),
    ]
