from rest_framework import serializers
from .models import Speed

class SpeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speed
        fields = ['id', 'vehicle', 'speed', 'created_at']
