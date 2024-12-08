import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from myapp.factories import SubnetFactory

client = APIClient()


@pytest.mark.django_db
def test_filter_by_company_id():
    # Создаём подсети с разными company_id
    SubnetFactory(company_id=1)
    SubnetFactory(company_id=2)

    url = reverse("filter")  # Убедитесь, что маршрут правильно настроен
    response = client.get(url, {"company_id": 1})

    # Проверяем, что фильтрация возвращает только нужные записи
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["company_id"] == 1


@pytest.mark.django_db
def test_filter_by_subnet():
    # Создаём подсети с разными значениями subnet
    subnet1 = SubnetFactory(subnet="192.168.1.0/24")
    subnet2 = SubnetFactory(subnet="10.0.0.0/8")

    url = reverse("filter")
    response = client.get(url, {"subnet": "192.168.1.0/24"})

    # Проверяем, что возвращается правильная подсеть
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["subnet"] == subnet1.subnet


@pytest.mark.django_db
def test_filter_by_id():
    # Создаём две подсети
    subnet1 = SubnetFactory()
    subnet2 = SubnetFactory()

    url = reverse("filter")
    response = client.get(url, {"id": subnet1.id})

    # Проверяем, что возвращается запись только по нужному ID
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["id"] == subnet1.id
