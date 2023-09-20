from unittest.mock import patch

import pytest
from django.contrib.auth.models import User
from django.core.management import call_command
from django.db import connections
from django.utils import timezone
from employees.models import Menu, Restaurant, Vote
from rest_framework.test import APIClient


@pytest.fixture(scope="function")
def django_db_setup(django_db_blocker):
    """
    This fixture sets up a test database with migrations
    """
    with django_db_blocker.unblock():
        for db_name in connections:
            call_command("migrate", database=db_name, verbosity=0)

        yield

        for db_name in connections:
            with patch('builtins.input', return_value='yes'):
                call_command("flush", database=db_name, verbosity=0)


@pytest.fixture(scope="session")
def client():
    return APIClient()


@pytest.fixture(scope="function")
def create_test_data(django_db_setup):
    restaurant = Restaurant.objects.create(name="Test Restaurant")
    user = User.objects.create(username="testuser")
    menu = Menu.objects.create(restaurant=restaurant, date=timezone.now(), items=["Item 1", "Item 2"])
    vote = Vote.objects.create(user=user, menu=menu, voted_at=timezone.now())

    return {"restaurant": restaurant, "user": user, "menu": menu, "vote": vote}
