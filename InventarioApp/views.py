from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from InventarioApp.models import Producto
from InventarioApp.serializers import ProductoSerializer

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