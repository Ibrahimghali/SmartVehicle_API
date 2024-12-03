from django.db import models
import uuid

class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    type = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    vin = models.CharField(max_length=17, blank=True, null=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.type})"
