import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from myapp.factories import SubnetFactory

client = APIClient()


@pytest.mark.django_db
def test_filter_by_company_id():
    SubnetFactory(company_id=1)
    SubnetFactory(company_id=2)

    url = reverse("filter")
    response = client.get(url, {"company_id": 1})

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["company_id"] == 1


@pytest.mark.django_db
def test_filter_by_subnet():
    SubnetFactory(subnet="192.168.1.0/24")
    SubnetFactory(subnet="10.0.0.0/8")

    url = reverse("filter")
    response = client.get(url, {"subnet": "192.168.1.0/24"})

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["subnet"] == "192.168.1.0/24"


@pytest.mark.django_db
def test_filter_by_id():
    subnet1 = SubnetFactory()
    SubnetFactory()

    url = reverse("filter")
    response = client.get(url, {"id": subnet1.id})

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["id"] == subnet1.id
