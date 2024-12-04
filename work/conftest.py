import pytest
import os
import django
from django.conf import settings


def pytest_configure():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    django.setup()


@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES["default"] = settings.DATABASES["test"]
