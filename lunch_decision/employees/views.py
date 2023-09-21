from collections import Counter

from django.utils import timezone
from rest_framework.decorators import (authentication_classes,
                                       permission_classes)
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Employee, Menu, Restaurant, Vote
from .permissions import IsAdminUserOrReadOnly
from .serializers import (EmployeeSerializer, MenuSerializer,
                          RestaurantSerializer, VoteSerializer)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUserOrReadOnly])
class RestaurantViewSet(ModelViewSet):
    """
    Viewset for managing restaurants.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUserOrReadOnly])
class MenuViewSet(ModelViewSet):
    """
    Viewset for managing menus.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUserOrReadOnly])
class VoteViewSet(ModelViewSet):
    """
    Viewset for managing votes.
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUserOrReadOnly])
class EmployeeViewSet(ModelViewSet):
    """
    Viewset for managing employees.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUserOrReadOnly])
class CurrentDayMenuView(RetrieveAPIView):
    """
    View for retrieving the menu with the most votes for the current day.
    """
    serializer_class = MenuSerializer

    def get_object(self):
        current_date = timezone.now().date()
        try:
            votes = Vote.objects.filter(menu__date=current_date)

            if not votes:
                return Menu.objects.get(date=current_date)

            menu_votes = Counter(vote.menu for vote in votes)
            winning_menu = max(menu_votes, key=menu_votes.get)
            return winning_menu
        except Menu.DoesNotExist:
            return None


@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUserOrReadOnly])
class CurrentDayResultsView(ListAPIView):
    """
    View for retrieving all votes made for the current day.
    """
    serializer_class = VoteSerializer

    def get_queryset(self):
        current_date = timezone.now().date()
        return Vote.objects.filter(menu__date=current_date)
