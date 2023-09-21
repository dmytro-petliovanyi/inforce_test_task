import pytest
from employees.models import Employee, Menu, Restaurant, Vote
from rest_framework import status


@pytest.mark.django_db
def test_create_employee(api_client, create_test_data):
    admin = create_test_data["admin"]
    api_client.force_authenticate(user=admin)

    user = create_test_data["user_2"]
    restaurant = create_test_data["restaurant"]

    data = {
        "user": user.id,
        "restaurant": restaurant.id,
        "position": "New Position",
    }

    response = api_client.post("/api/employees/", data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    employee = Employee.objects.get(id=response.data["id"])
    assert employee.user == user
    assert employee.restaurant.name == "Test Restaurant"
    assert employee.position == "New Position"


@pytest.mark.django_db
def test_create_menu(api_client, create_test_data):
    admin = create_test_data["admin"]
    api_client.force_authenticate(user=admin)

    restaurant = create_test_data["restaurant"]

    data = {
        "restaurant": restaurant.id,
        "date": "2023-09-20",
        "items": ["New Item 1", "New Item 2"],
    }

    response = api_client.post("/api/menus/", data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    menu = Menu.objects.get(id=response.data.get("id"))
    assert menu.restaurant == restaurant
    assert menu.date.strftime("%Y-%m-%d") == "2023-09-20"
    assert menu.items == ["New Item 1", "New Item 2"]


@pytest.mark.django_db
def test_create_restaurant(api_client, create_test_data):
    admin = create_test_data["admin"]
    api_client.force_authenticate(user=admin)
    data = {
        "name": "New Restaurant",
    }

    response = api_client.post("/api/restaurants/", data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Restaurant.objects.get(name="New Restaurant").name == "New Restaurant"


@pytest.mark.django_db
def test_create_vote(api_client, create_test_data):
    admin = create_test_data["admin"]
    api_client.force_authenticate(user=admin)

    user = create_test_data["user"]
    menu = create_test_data["menu"]

    data = {
        "user": user.id,
        "menu": menu.id,
    }

    response = api_client.post("/api/votes/", data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    vote = Vote.objects.get(id=response.data["id"])
    assert vote.user == user
    assert vote.menu == menu


@pytest.mark.django_db
def test_get_menu_detail(api_client, create_test_data):
    admin = create_test_data["admin"]
    api_client.force_authenticate(user=admin)

    menu = create_test_data["menu"]
    response = api_client.get("/api/menus/")
    response_data = response.data[0]

    assert response.status_code == status.HTTP_200_OK
    assert response_data.get("restaurant") == menu.restaurant.id
    assert response_data["date"] == menu.date.strftime("%Y-%m-%d")
    assert response_data["items"] == menu.items


@pytest.mark.django_db
def test_get_employee_detail(api_client, create_test_data):
    admin = create_test_data["admin"]
    api_client.force_authenticate(user=admin)

    employee = create_test_data["employee"]
    response = api_client.get("/api/employees/")
    response_data = response.data[0]

    assert response.status_code == status.HTTP_200_OK
    assert response_data.get("restaurant") == employee.restaurant.id
    assert response_data["position"] == employee.position
    assert response_data["user"] == employee.user.id


@pytest.mark.django_db
def test_get_restaurant_detail(api_client, create_test_data):
    admin = create_test_data["admin"]
    api_client.force_authenticate(user=admin)

    restaurant = create_test_data["restaurant"]
    response = api_client.get("/api/restaurants/")
    response_data = response.data[0]

    assert response.status_code == status.HTTP_200_OK
    assert response_data["name"] == restaurant.name
