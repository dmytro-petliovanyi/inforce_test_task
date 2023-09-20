from unittest.mock import patch

import pytest
from django.core.management import call_command
from django.db import connections
from django.test import Client


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
    return Client()
