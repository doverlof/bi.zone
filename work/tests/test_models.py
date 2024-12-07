import pytest
from django.core.exceptions import ValidationError
from myapp.factories import SubnetFactory


@pytest.mark.django_db
def test_create_subnet_with_valid_ip():
    subnet = SubnetFactory(subnet="192.168.1.0/24")
    try:
        subnet.save()
    except ValidationError:
        pytest.fail("ValidationError raised unexpectedly with valid IP address")
    assert subnet.subnet == "192.168.1.0/24"


@pytest.mark.django_db
def test_create_subnet_with_invalid_ip():
    subnet = SubnetFactory.build(subnet="192.268.1.0/24")
    with pytest.raises(ValidationError) as excinfo:
        subnet.save()
    assert "Введите корректное значение IP-адреса с маской в формате CIDR" in str(
        excinfo.value
    )


@pytest.mark.django_db
def test_create_subnet_with_invalid_format():
    # Создаем объект с некорректным форматом IP-адреса
    subnet = SubnetFactory.build(subnet="invalid_cidr_format")
    with pytest.raises(ValidationError) as excinfo:
        subnet.save()
    assert "Введите корректное значение IP-адреса с маской в формате CIDR" in str(
        excinfo.value
    )
