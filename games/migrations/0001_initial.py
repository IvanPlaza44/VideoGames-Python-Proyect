# Generated by Django 4.1.1 on 2022-11-05 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videojuegos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('desarrollador', models.CharField(max_length=40)),
                ('genero', models.CharField(max_length=40)),
                ('plataformas', models.CharField(max_length=40)),
                ('precio', models.IntegerField()),
                ('jugadores', models.CharField(max_length=40)),
                ('lanzamiento', models.DateField()),
                ('resumen', models.CharField(max_length=40)),
            ],
        ),
    ]