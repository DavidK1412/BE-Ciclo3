from django.db.models import fields
from adminAuth.models.factura import Factura
from rest_framework import serializers
class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ['cliente']