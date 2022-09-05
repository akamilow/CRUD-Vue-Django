from django.db import models

# Create your models here.

class Producto(models.Model):
    producto_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    precio = models.IntegerField()
    cantidad = models.IntegerField()

class Cocina(models.Model):
    id_pro_cocina = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    proveedor = models.CharField(max_length=100)

class Limpieza(models.Model):
    id_pro_limpieza = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    proveedor = models.CharField(max_length=100)

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    producto = models.CharField(max_length=100)
    fecha = models.DateField()
    precio_total = models.IntegerField()