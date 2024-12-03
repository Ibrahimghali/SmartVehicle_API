from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework import status
from .models import Location
from .serializers import LocationSerializer

class LocationListCreateViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
    ViewSet for listing and creating Location records.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get_queryset(self):
        vehicle_id = self.request.query_params.get('vehicle_id')
        
        if vehicle_id is not None:
            return Location.objects.filter(vehicle=vehicle_id)
        
        return Location.objects.none()

    def list(self, request, *args, **kwargs):
        vehicle_id = self.request.query_params.get('vehicle_id')
        
        if vehicle_id is None:
            # If no vehicle ID is provided, return a 400 error response
            return Response(
                {"message": "The ID of the vehicle is not provided"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Use the filtered queryset
        return super().list(request, *args, **kwargs)


class LocationRetrieveUpdateDestroyViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, 
                                           mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """
    ViewSet for retrieving, updating, and destroying Location records.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
