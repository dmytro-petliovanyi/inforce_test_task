from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import (authentication_classes,
                                       permission_classes)
from rest_framework.response import Response
from rest_framework.views import APIView
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


@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUserOrReadOnly])
class CurrentDayMenuView(APIView):
    def get(self, request):
        current_date = timezone.now().date()
        try:
            menu = Menu.objects.get(date=current_date)
            serializer = MenuSerializer(menu)
            return Response(serializer.data)

        except Menu.DoesNotExist:
            return Response({"detail": "Menu for today not found."}, status=status.HTTP_404_NOT_FOUND)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUserOrReadOnly])
class CurrentDayResultsView(APIView):
    def get(self, request):
        current_date = timezone.now().date()
        try:
            votes = Vote.objects.filter(menu__date=current_date)
            serializer = VoteSerializer(votes, many=True)
            return Response(serializer.data)
        except Vote.DoesNotExist:
            return Response({"detail": "No votes for today yet."}, status=status.HTTP_404_NOT_FOUND)
