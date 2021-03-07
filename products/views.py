from .models import CoffeeMachine, CoffeePod
from rest_framework import viewsets
from rest_framework import permissions
from products.serializers import CoffeePodSerializer, CoffeeMachineSerializer


class CoffeeMachineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Coffee Machines to be viewed or edited.
    """
    queryset = CoffeeMachine.objects.all()
    serializer_class = CoffeeMachineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_fields = ['machine_type', 'water_line_compatible', 'model']


class CoffeePodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Coffee Pods to be viewed or edited.
    """
    queryset = CoffeePod.objects.all()
    serializer_class = CoffeePodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_fields = ['pod_type', 'flavor', 'package_size']