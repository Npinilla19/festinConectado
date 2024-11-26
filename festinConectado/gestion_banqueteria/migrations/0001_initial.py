# Generated by Django 5.1.3 on 2024-11-20 22:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banqueteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_servicio', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('direccion', models.CharField(max_length=200)),
                ('comuna', models.CharField(max_length=100)),
                ('tipo_evento', models.CharField(max_length=50)),
                ('precio_estimado', models.FloatField()),
                ('disponibilidad', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('tipo_usuario', models.CharField(choices=[('clientes', 'Clientes'), ('proveedor', 'Proveedor')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_evento', models.DateTimeField(auto_now_add=True)),
                ('mensaje', models.TextField()),
                ('banqueteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_banqueteria.banqueteria')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_banqueteria.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='banqueteria',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_banqueteria.usuario'),
        ),
    ]
