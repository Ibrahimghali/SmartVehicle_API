from django.db import models
from vehicle.models import Vehicle  # Import the Vehicle model
import uuid

class FuelConsumption(models.Model):
    FUEL_UNITS = [
        ('liters', 'Liters'),
        ('gallons', 'Gallons'),
    ]

    EFFICIENCY_UNITS = [
        ('km/l', 'Kilometers per Liter'),
        ('mpg', 'Miles per Gallon'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='fuel_consumptions',
        help_text="The vehicle associated with this fuel consumption entry"
    )
    fuel_used = models.FloatField(
        help_text="Amount of fuel used in liters or gallons"
    )
    fuel_efficiency = models.FloatField(
        help_text="Fuel efficiency (e.g., km/l or mpg)"
    )
    unit = models.CharField(
        max_length=10,
        choices=FUEL_UNITS,
        default='liters',
        help_text="Unit of fuel used"
    )
    efficiency_unit = models.CharField(
        max_length=10,
        choices=EFFICIENCY_UNITS,
        default='km/l',
        help_text="Unit of fuel efficiency"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the fuel consumption data was recorded"
    )

    def __str__(self):
        return f"Fuel: {self.fuel_used} {self.unit}, Efficiency: {self.fuel_efficiency} {self.efficiency_unit} (Vehicle ID: {self.vehicle.id})"
