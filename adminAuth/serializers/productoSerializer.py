from adminAuth.models.producto import Producto
from rest_framework import serializers

class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nom_prod', 'id_Prod', 'LINKImg', 'Descripcion', 'ProdInven', 'Precio']
    

    def create(self, validated_data):
        productInstance = Producto.objects.create(**validated_data)
        return productInstance

    def update(self, instance, validated_data):
        updated_data = super().update(instance, validated_data)
        updated_data.save()
        return updated_data

    def to_representation(self, obj):
        producto = Producto.objects.get(id_Prod=obj.id_Prod)
        return {
                    'id_Prod': producto.id_Prod,
                    'nom_prod': producto.nom_prod,
                    'LINKImg': producto.LINKImg,
                    'Descripcion': producto.Descripcion,
                    'ProdInven': producto.ProdInven,
                    'Precio': producto.Precio 
        }