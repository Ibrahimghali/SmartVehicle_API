from django.urls import path
from .views import VehicleListCreateViewSet, VehicleRetrieveUpdateDestroyViewSet

urlpatterns = [
    # URL for listing and creating vehicles
    path('', VehicleListCreateViewSet.as_view({'get': 'list', 'post': 'create'}), name='vehicle-list-create'),
    
    # URL for retrieving, updating, and deleting a specific vehicle
    path('<str:pk>/', VehicleRetrieveUpdateDestroyViewSet.as_view({
        'get': 'retrieve',   # Retrieve a specific vehicle by ID
        'put': 'update',     # Update a specific vehicle by ID
        'patch': 'partial_update',  # Partially update a specific vehicle by ID
        'delete': 'destroy'  # Delete a specific vehicle by ID
    }), name='vehicle-retrieve-update-destroy'),
]
