from django.urls import path
from .views import LocationListCreateViewSet, LocationRetrieveUpdateDestroyViewSet

urlpatterns = [
    # URL for listing and creating location records
    path('', LocationListCreateViewSet.as_view({'get': 'list', 'post': 'create'}), name='location-list-create'),
    
    # URL for retrieving, updating, and deleting a specific location record
    path('<str:pk>/', LocationRetrieveUpdateDestroyViewSet.as_view({
        'get': 'retrieve',   # Retrieve a specific location record by ID
        'put': 'update',     # Fully update a specific location record by ID
        'patch': 'partial_update',  # Partially update a specific location record by ID
        'delete': 'destroy'  # Delete a specific location record by ID
    }), name='location-retrieve-update-destroy'),
]
