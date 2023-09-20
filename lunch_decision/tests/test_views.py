import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from employees.models import Menu, Restaurant, Vote


@pytest.fixture(scope="function")
def create_test_data(django_db_setup):
    restaurant = Restaurant.objects.create(name="Test Restaurant")
    user = User.objects.create(username="testuser")
    menu = Menu.objects.create(restaurant=restaurant, date=timezone.now(), items=["Item 1", "Item 2"])
    vote = Vote.objects.create(user=user, menu=menu, voted_at=timezone.now())

    return {"restaurant": restaurant, "user": user, "menu": menu, "vote": vote}


def test_create_restaurant(create_test_data):
    restaurant = create_test_data["restaurant"]
    assert restaurant.name == "Test Restaurant"


def test_create_menu(create_test_data):
    menu = create_test_data["menu"]
    assert menu.items == ["Item 1", "Item 2"]


def test_create_vote(create_test_data):
    user, vote = create_test_data["user"], create_test_data["vote"]
    assert vote.user == user
