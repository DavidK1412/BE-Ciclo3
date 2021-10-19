from rest_framework import serializers
from adminAuth.models.admin import Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'username', 'password', 'email', 'nombre']
    
    def crear(self, validated_data):
        adminInstance = Admin.objects.create(**validated_data)
        return adminInstance

    def to_representation(self, obj): 
        admin = Admin.objects.get(id = obj.id)
        return {
            'id': admin.id,
            'username': admin.username,
            'password': admin.password,
            'email': admin.email,
            'nombre': admin.nombre,
        }