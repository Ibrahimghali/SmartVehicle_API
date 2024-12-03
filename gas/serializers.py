from rest_framework import serializers
from .models import VehicleGasSensor

class VehicleGasSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleGasSensor
        fields = [
            'id', 'gas_type', 'temperature', 'unit',
            'gas_concentration', 'concentration_unit', 
            'created_at', 'vehicle'
        ]
