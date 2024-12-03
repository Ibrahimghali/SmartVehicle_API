from django.urls import path
from .views import SpeedListCreateViewSet, SpeedRetrieveUpdateDestroyViewSet

urlpatterns = [
    # URL for listing and creating speed records
    path('', SpeedListCreateViewSet.as_view({'get': 'list', 'post': 'create'}), name='speed-list-create'),
    
    # URL for retrieving, updating, and deleting a specific speed record
    path('<str:pk>/', SpeedRetrieveUpdateDestroyViewSet.as_view({
        'get': 'retrieve',   # Retrieve a specific speed record by ID
        'put': 'update',     # Fully update a specific speed record by ID
        'patch': 'partial_update',  # Partially update a specific speed record by ID
        'delete': 'destroy'  # Delete a specific speed record by ID
    }), name='speed-retrieve-update-destroy'),
]
