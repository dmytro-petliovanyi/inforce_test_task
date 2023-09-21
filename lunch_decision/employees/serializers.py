from rest_framework.serializers import ModelSerializer

from .models import Employee, Menu, Restaurant, Vote


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class VoteSerializer(ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
