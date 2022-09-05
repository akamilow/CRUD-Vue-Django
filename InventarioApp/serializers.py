from rest_framework import serializers
from InventarioApp.models import Producto
from InventarioApp.models import Cocina
from InventarioApp.models import Limpieza
from InventarioApp.models import Proveedor

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('producto_id', 'nombre', 'categoria', 'precio', 'cantidad')
        extra_kwargs = {
            'nombre': {'required': True},
            'categoria': {'required': True},
            'precio': {'required': True},
            'cantidad': {'required': True},
        }

class CocinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocina
        fields = ('id_pro_cocina', 'nombre', 'cantidad', 'precio', 'proveedor')
        extra_kwargs = {
            'nombre': {'required': True},
            'cantidad': {'required': True},
            'precio': {'required': True},
            'proveedor': {'required': True},
        }

class LimpiezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Limpieza
        fields = ('id_pro_limpieza', 'nombre', 'cantidad', 'precio', 'proveedor')
        extra_kwargs = {
            'nombre': {'required': True},
            'cantidad': {'required': True},
            'precio': {'required': True},
            'proveedor': {'required': True},
        }

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('id_proveedor', 'nombre', 'telefono', 'direccion', 'correo', 'producto', 'fecha', 'precio_total')
        extra_kwargs = {
            'nombre': {'required': True},
            'telefono': {'required': True},
            'direccion': {'required': True},
            'correo': {'required': True},
            'producto': {'required': True},
            'fecha': {'required': True},
            'precio_total': {'required': True},
        }