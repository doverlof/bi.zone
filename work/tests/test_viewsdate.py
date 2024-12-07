import pytest
from datetime import datetime
from unittest.mock import patch
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from myapp.factories import SubnetFactory

client = APIClient()


@pytest.mark.django_db
@patch(
    "django.db.models.fields.DateTimeField.pre_save",
    lambda self, obj, add: obj.created_at,
)
def test_filter_after_date():
    date1 = timezone.make_aware(datetime(2024, 1, 1, 12, 0, 0))
    date2 = timezone.make_aware(datetime(2024, 3, 1, 12, 0, 0))
    date3 = timezone.make_aware(datetime(2024, 5, 1, 12, 0, 0))

    SubnetFactory(created_at=date1)
    SubnetFactory(created_at=date2)
    SubnetFactory(created_at=date3)

    url = reverse("filter")

    response = client.get(url, {"after_date": "2024-02-01T00:00:00Z"})

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2


@pytest.mark.django_db
@patch(
    "django.db.models.fields.DateTimeField.pre_save",
    lambda self, obj, add: obj.created_at,
)
def test_filter_before_date():
    date1 = timezone.make_aware(datetime(2024, 1, 1, 12, 0, 0))
    date2 = timezone.make_aware(datetime(2024, 3, 1, 12, 0, 0))
    date3 = timezone.make_aware(datetime(2024, 5, 1, 12, 0, 0))

    SubnetFactory(created_at=date1)
    SubnetFactory(created_at=date2)
    SubnetFactory(created_at=date3)

    url = reverse("filter")

    response = client.get(url, {"before_date": "2024-02-01T00:00:00Z"})

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


@pytest.mark.django_db
@patch(
    "django.db.models.fields.DateTimeField.pre_save",
    lambda self, obj, add: obj.created_at,
)
def test_filter_between_date():
    date1 = timezone.make_aware(datetime(2024, 1, 1, 12, 0, 0))
    date2 = timezone.make_aware(datetime(2024, 3, 1, 12, 0, 0))
    date3 = timezone.make_aware(datetime(2024, 5, 1, 12, 0, 0))

    SubnetFactory(created_at=date1)
    SubnetFactory(created_at=date2)
    SubnetFactory(created_at=date3)

    url = reverse("filter")

    response = client.get(
        url,
        {"after_date": "2024-02-01T00:00:00Z", "before_date": "2024-04-01T00:00:00Z"},
    )

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
