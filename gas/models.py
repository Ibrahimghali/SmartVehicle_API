from django.db import models
from vehicle.models import Vehicle  # Import the Vehicle model

import uuid

class VehicleGasSensor(models.Model):
    GAS_TYPES = [
        ('CO', 'Carbon Monoxide'),
        ('CO2', 'Carbon Dioxide'),
        ('CH4', 'Methane'),
        ('O2', 'Oxygen'),
        ('VOC', 'Volatile Organic Compounds'),
    ]

    UNIT_CHOICES = [
        ('C', 'Celsius'),
        ('F', 'Fahrenheit'),
    ]

    CONCENTRATION_UNITS = [
        ('ppm', 'Parts Per Million'),
        ('ppb', 'Parts Per Billion'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    gas_type = models.CharField(
        max_length=10,
        choices=GAS_TYPES,
        default='CO',
        help_text="Type of gas being measured"
    )
    temperature = models.FloatField(
        help_text="Temperature in the environment"
    )
    unit = models.CharField(
        max_length=2,
        choices=UNIT_CHOICES,
        default='C',
        help_text="Unit of temperature"
    )
    gas_concentration = models.FloatField(
        help_text="Concentration of the gas"
    )
    concentration_unit = models.CharField(
        max_length=5,
        choices=CONCENTRATION_UNITS,
        default='ppm',
        help_text="Unit of gas concentration"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the data was recorded"
    )
    vehicle = models.ForeignKey(
        Vehicle,  # The related Vehicle model
        on_delete=models.CASCADE,  # Delete associated sensor data when the vehicle is deleted
        related_name='gas_sensors',  # Access all sensors from a vehicle instance
        help_text="The vehicle associated with this gas sensor"
    )

    def __str__(self):
        return f"{self.gas_type} - {self.gas_concentration}{self.concentration_unit} at {self.temperature}{self.unit} (Vehicle ID: {self.vehicle.id})"
