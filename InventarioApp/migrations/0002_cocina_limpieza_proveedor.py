# Generated by Django 4.1 on 2022-09-05 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InventarioApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cocina',
            fields=[
                ('id_pro_cocina', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('proveedor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Limpieza',
            fields=[
                ('id_pro_limpieza', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('proveedor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('producto', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('precio_total', models.IntegerField()),
            ],
        ),
    ]
