from rest_framework import viewsets, mixins
from .models import Vehicle
from .serializers import VehicleSerializer

class VehicleListCreateViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
    ViewSet for listing and creating Vehicle records.
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class VehicleRetrieveUpdateDestroyViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, 
                                          mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """
    ViewSet for retrieving, updating, and destroying Vehicle records.
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
