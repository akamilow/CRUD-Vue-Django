from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from InventarioApp.models import Producto
from InventarioApp.serializers import ProductoSerializer
from InventarioApp.models import Cocina
from InventarioApp.serializers import CocinaSerializer
from InventarioApp.models import Limpieza
from InventarioApp.serializers import LimpiezaSerializer
from InventarioApp.models import Proveedor
from InventarioApp.serializers import ProveedorSerializer

# Create your views here.

@csrf_exempt
def producto_list(request, id=0):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        producto_data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=producto_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Cargado en base de datos: ", safe=False)
        return JsonResponse("Error: ", safe=False)
    elif request.method == 'PUT':
        producto_data = JSONParser().parse(request)
        producto = Producto.objects.get(producto_id = producto_data['producto_id'])
        serializer = ProductoSerializer(producto, data=producto_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Actualizado en base de datos: ", safe=False)
        return JsonResponse("Error: ", safe=False) 
    elif request.method == 'DELETE':
        producto = Producto.objects.get(producto_id=id)
        producto.delete()
        return JsonResponse("Eliminado de base de datos: ", safe=False)

@csrf_exempt
def cocina_list(request, id=0):
    if request.method == 'GET':
        cocinas = Cocina.objects.all()
        serializer = CocinaSerializer(cocinas, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        cocina_data = JSONParser().parse(request)
        serializer = CocinaSerializer(data=cocina_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Cargado en base de datos: ", safe=False)
        return JsonResponse("Error: ", safe=False)
    elif request.method == 'PUT':
        cocina_data = JSONParser().parse(request)
        cocina = Cocina.objects.get(id_pro_cocina = cocina_data['id_pro_cocina'])
        serializer = CocinaSerializer(cocina, data=cocina_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Actualizado en base de datos: ", safe=False)
        return JsonResponse("Error: ", safe=False) 
    elif request.method == 'DELETE':
        cocina = Cocina.objects.get(id_pro_cocina=id)
        cocina.delete()
        return JsonResponse("Eliminado de base de datos: ", safe=False)

@csrf_exempt
def limpieza_list(request, id=0):
    if request.method == 'GET':
        limpiezas = Limpieza.objects.all()
        serializer = LimpiezaSerializer(limpiezas, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        limpieza_data = JSONParser().parse(request)
        serializer = LimpiezaSerializer(data=limpieza_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Cargado en base de datos: ", safe=False)
        return JsonResponse("Error: ", safe=False)
    elif request.method == 'PUT':
        limpieza_data = JSONParser().parse(request)
        limpieza = Limpieza.objects.get(id_pro_limpieza = limpieza_data['id_pro_limpieza'])
        serializer = LimpiezaSerializer(limpieza, data=limpieza_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Actualizado en base de datos: ", safe=False)
        return JsonResponse("Error: ", safe=False) 
    elif request.method == 'DELETE':
        limpieza = Limpieza.objects.get(id_pro_limpieza=id)
        limpieza.delete()
        return JsonResponse("Eliminado de base de datos: ", safe=False)

@csrf_exempt
def proveedor_list(request, id=0):
    if request.method == 'GET':
        proveedores = Proveedor.objects.all()
        serializer = ProveedorSerializer(proveedores, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        proveedor_data = JSONParser().parse(request)
        serializer = ProveedorSerializer(data=proveedor_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Cargado en base de datos: ", safe=False)
        return JsonResponse("Error: ", safe=False)
    elif request.method == 'PUT':
        proveedor_data = JSONParser().parse(request)
        proveedor = Proveedor.objects.get(id_proveedor = proveedor_data['id_proveedor'])
        serializer = ProveedorSerializer(proveedor, data=proveedor_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Actualizado en base de datos: ", safe=False)
        return JsonResponse("Error: ", safe=False) 
    elif request.method == 'DELETE':
        proveedor = Proveedor.objects.get(id_proveedor=id)
        proveedor.delete()
        return JsonResponse("Eliminado de base de datos: ", safe=False)