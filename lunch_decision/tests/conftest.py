import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from employees.models import Employee, Menu, Restaurant, Vote
from rest_framework.test import APIClient


@pytest.fixture(scope="function")
def create_test_data():
    admin_user = User.objects.create(username="admin")
    admin_user.is_staff = True
    admin_user.is_superuser = True
    admin_user.set_password("admin_password")
    admin_user.save()
    restaurant = Restaurant.objects.create(name="Test Restaurant")
    user = User.objects.create(username="testuser")
    user_2 = User.objects.create(username="testuser2")
    menu = Menu.objects.create(restaurant=restaurant, date=timezone.now(), items=["Item 1", "Item 2"])
    vote = Vote.objects.create(user=user, menu=menu, voted_at=timezone.now())
    employee = Employee.objects.create(user=user, restaurant=restaurant, position="Test Position")

    return {"restaurant": restaurant, "user": user, "user_2": user_2, "menu": menu, "vote": vote, "employee": employee,
            "admin": admin_user}


@pytest.fixture(scope="session")
def api_client():
    return APIClient()
