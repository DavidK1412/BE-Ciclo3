from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from adminAuth.models.venta import Venta
from adminAuth.models.factura import Factura
from adminAuth.serializers.facturaSerializer import FacturaSerializer
import adminAuth.views.productoCreateview

class VentaSerializer(serializers.ModelSerializer):
    factura = FacturaSerializer()
    class Meta:
        model = Venta
        fields = ['id', 'fechaVenta', 'valor', 'descuento', 'productList', 'factura', 'valorTotal']
    
    def create(self, validated_data):
        facturaData = validated_data.pop('factura')
        validated_data['valor'] = adminAuth.views.productoCreateview.sum_prices(validated_data['productList'])
        if validated_data['valor'] < validated_data['descuento']:
            raise ValueError('El descuento es mayor que el valor de la factura')
        validated_data['valorTotal'] = validated_data['valor'] - validated_data['descuento'] 
        adminAuth.views.productoCreateview.update_inv(validated_data['productList'])  
        ventaInstance = Venta.objects.create(**validated_data)
        Factura.objects.create(venta=ventaInstance, **facturaData)
        return ventaInstance
    
    def to_representation(self, obj):
        venta = Venta.objects.get(id=obj.id)
        factura = Factura.objects.get(venta=obj.id)
        return{
            'id': venta.id,
            'fechaVenta': venta.fechaVenta,
            'valor': venta.valor,
            'descuento': venta.descuento,
            'valorTotal': venta.valorTotal,
            'productList': venta.productList,
            'factura': {
                'id': factura.id,
                'cliente': factura.cliente,
            }
        }