from rest_framework.decorators import (authentication_classes,
                                       permission_classes)
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Employee, Menu, Restaurant, Vote
from .permissions import IsAdminUserOrReadOnly
from .serializers import (EmployeeSerializer, MenuSerializer,
                          RestaurantSerializer, VoteSerializer)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUserOrReadOnly])
class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUserOrReadOnly])
class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUserOrReadOnly])
class VoteViewSet(ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUserOrReadOnly])
class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
