from django.urls import path
from .views import VehicleGasSensorListCreateViewSet, VehicleGasSensorRetrieveUpdateDestroyViewSet

urlpatterns = [
    # URL for listing and creating gas sensor records
    path('', VehicleGasSensorListCreateViewSet.as_view({'get': 'list', 'post': 'create'}), name='vehicle-gas-sensor-list-create'),
    
    # URL for retrieving, updating, and deleting a specific gas sensor record
    path('<str:pk>/', VehicleGasSensorRetrieveUpdateDestroyViewSet.as_view({
        'get': 'retrieve',   # Retrieve a specific gas sensor record by ID
        'put': 'update',     # Fully update a specific gas sensor record by ID
        'patch': 'partial_update',  # Partially update a specific gas sensor record by ID
        'delete': 'destroy'  # Delete a specific gas sensor record by ID
    }), name='vehicle-gas-sensor-retrieve-update-destroy'),
]
