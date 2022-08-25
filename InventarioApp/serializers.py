from rest_framework import serializers
from InventarioApp.models import Producto

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