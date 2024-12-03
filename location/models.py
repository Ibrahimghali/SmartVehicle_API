from django.db import models
from vehicle.models import Vehicle

import uuid

class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="locations")
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Vehicle {self.vehicle.id} - Location ({self.latitude}, {self.longitude}) at {self.created_at}"
