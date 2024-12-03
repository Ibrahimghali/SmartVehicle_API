from django.urls import path
from .views import FuelConsumptionListCreateViewSet, FuelConsumptionRetrieveUpdateDestroyViewSet

urlpatterns = [
    # URL for listing and creating fuel consumption records
    path('', FuelConsumptionListCreateViewSet.as_view({'get': 'list', 'post': 'create'}), name='fuel-consumption-list-create'),
    
    # URL for retrieving, updating, and deleting a specific fuel consumption record
    path('<str:pk>/', FuelConsumptionRetrieveUpdateDestroyViewSet.as_view({
        'get': 'retrieve',   # Retrieve a specific fuel consumption record by ID
        'put': 'update',     # Fully update a specific fuel consumption record by ID
        'patch': 'partial_update',  # Partially update a specific fuel consumption record by ID
        'delete': 'destroy'  # Delete a specific fuel consumption record by ID
    }), name='fuel-consumption-retrieve-update-destroy'),
]
