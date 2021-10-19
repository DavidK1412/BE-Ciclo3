from rest_framework import status
from rest_framework import response
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from adminAuth.models import Venta, Factura, Producto
from adminAuth.serializers import VentaSerializer

@api_view(['POST', 'GET'])
@permission_classes((IsAuthenticated, ))
def venta_api(request):
    if request.method == 'POST':
        print(request.data['descuento'])
        venta_serializer = VentaSerializer(data=request.data)
        if venta_serializer.is_valid():
            venta_serializer.save()
            return Response({'response': 'Exitosamente'}, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        ventas = Venta.objects.all()
        venta_serializer = VentaSerializer(ventas, many= True)
        return Response(venta_serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def venta_detail(request, pk):
    try:
        venta = Venta.objects.get(pk = pk)
    except Venta.DoesNotExist:
        return Response({'response': 'No existe ese producto!'}, status = status.HTTP_404_NOT_FOUND )
    
    if request.method == 'GET':
        venta_serializer = VentaSerializer(venta)
        return Response(venta_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        factura = Factura.objects.get(pk = pk)
        venta.delete()
        factura.delete()
        return Response({'response': 'Venta eliminada!'})