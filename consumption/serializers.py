from rest_framework import serializers
from .models import FuelConsumption

class FuelConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelConsumption
        fields = [
            'id', 'vehicle', 'fuel_used', 'fuel_efficiency',
            'unit', 'efficiency_unit', 'created_at'
        ]
