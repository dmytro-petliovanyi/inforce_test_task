from employees.models import Restaurant, Vote
from rest_framework import status


def test_get_menu_detail(client, create_test_data):
    menu = create_test_data["menu"]
    response = client.get("/api/menus/")
    response_data = response.data[0]

    assert response.status_code == status.HTTP_200_OK
    assert response_data.get("restaurant") == menu.restaurant.id
    assert response_data["date"] == menu.date.strftime("%Y-%m-%d")
    assert response_data["items"] == menu.items


def test_get_restaurant_detail(client, create_test_data):
    restaurant = create_test_data["restaurant"]
    response = client.get("/api/restaurants/")
    response_data = response.data[0]

    assert response.status_code == status.HTTP_200_OK
    assert response_data["name"] == restaurant.name


def test_get_vote_detail(client, create_test_data):
    vote = create_test_data["vote"]
    response = client.get("/api/votes/")
    response_data = response.data[0]

    assert response.status_code == status.HTTP_200_OK
    assert response_data.get("user") == vote.user.id
    assert response_data.get("menu") == vote.menu.id


def test_create_restaurant(client, django_db_setup):
    data = {
        "name": "New Restaurant",
    }

    response = client.post("/api/restaurants/", data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Restaurant.objects.get(name="New Restaurant").name == "New Restaurant"


def test_create_vote(client, create_test_data):
    user = create_test_data["user"]
    menu = create_test_data["menu"]

    data = {
        "user": user.id,
        "menu": menu.id,
    }

    response = client.post("/api/votes/", data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    vote = Vote.objects.get(id=response.data["id"])
    assert vote.user == user
    assert vote.menu == menu
