import pytest
from django.utils import timezone
from employees.models import Menu
from rest_framework import status


@pytest.mark.django_db
def test_get_current_day_menu(api_client, create_test_data):
    current_date = timezone.now().date()
    restaurant = create_test_data["restaurant"]
    Menu.objects.create(date=current_date, items=["Item 1", "Item 2"], restaurant=restaurant)

    response = api_client.get("/api/current-day-menu/")
    assert response.status_code == status.HTTP_200_OK

    assert response.data[0]["id"] == create_test_data["menu"].id


@pytest.mark.django_db
def test_current_day_results_view(api_client, create_test_data):

    vote = create_test_data["vote"]

    api_client.force_authenticate(user=vote.user)

    response = api_client.get("/api/current-day-results/")

    assert response.status_code == status.HTTP_200_OK

    assert len(response.data) == 1
    assert response.data == 0
    assert response.data[0]["user"] == vote.user.id
    assert response.data[0]["menu"] == vote.menu.id
