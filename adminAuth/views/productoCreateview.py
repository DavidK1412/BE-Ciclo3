from types import DynamicClassAttribute
from rest_framework import status
from rest_framework import response
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from adminAuth.models import Producto
from adminAuth.serializers import productoSerializer

def update_inv(dict):
    json = eval(dict)
    for k, v in json.items():
        pk = int(k)
        value = int(v)
        producto = Producto.objects.get(pk=pk)
        if producto.ProdInven < value:
            raise ValueError('Cantidad solicitadas sobrepasa nuestro inventario!')
        producto.ProdInven =  producto.ProdInven - value
        producto.save()

def sum_prices(dict):
    json = eval(dict)
    total = 0
    for k, v in json.items():
        pk = int(k)
        value = int(v)
        producto = Producto.objects.get(pk=pk)
        for i in range(value):
            total += producto.Precio
    return total 


@api_view(['POST', 'GET'])
@permission_classes((IsAuthenticated , ))
def producto_api(request):
    if request.method == 'POST':
        producto_serializer = productoSerializer(data = request.data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response({'response':'Producto creado!'}, status=status.HTTP_201_CREATED)
        return Response(producto_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        productos = Producto.objects.all()
        producto_serializer = productoSerializer(productos, many = True)
        return Response(producto_serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def producto_detail(request, pk):
    try:
        producto = Producto.objects.get(pk = pk)
    except Producto.DoesNotExist:
        return Response({'response': 'No existe ese producto'}, status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        producto_serializer = productoSerializer(producto)
        return Response(producto_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        producto_serializer = productoSerializer(producto, data = request.data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        producto.delete()
        return Response({'response': 'Producto eliminado!'}, status=status.HTTP_200_OK)
    