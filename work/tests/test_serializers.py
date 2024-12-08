import pytest
from myapp.serializers import SubnetSerializer
from myapp.factories import SubnetFactory


@pytest.mark.django_db
def test_subnet_serializer_with_valid_data():
    valid_data = {
        "subnet": "192.168.1.0/24",
        "company_id": 1,
    }
    serializer = SubnetSerializer(data=valid_data)
    assert (
        serializer.is_valid()
    ), "Сериализатор должен быть валидным при корректных данных"
    instance = serializer.save()
    assert instance.subnet == valid_data["subnet"]
    assert instance.company_id == valid_data["company_id"]


@pytest.mark.django_db
def test_subnet_serializer_with_invalid_data():
    invalid_data = {
        "subnet": "192.268.1.0/24",
        "company_id": 1,
    }
    serializer = SubnetSerializer(data=invalid_data)
    assert (
        not serializer.is_valid()
    ), "Сериализатор должен быть невалидным при некорректных данных"
    assert "subnet" in serializer.errors, "Ошибка должна быть в поле 'subnet'"


@pytest.mark.django_db
def test_subnet_serializer_serialization():
    subnet_instance = SubnetFactory(subnet="192.168.1.0/24", company_id=1)
    serializer = SubnetSerializer(instance=subnet_instance)
    data = serializer.data
    expected_fields = {"id", "subnet", "company_id", "created_at"}

    assert (
        set(data.keys()) == expected_fields
    ), "Поля выходных данных не совпадают с ожидаемыми"

    assert (
        data["subnet"] == "192.168.1.0/24"
    ), "Поле 'subnet' содержит неверное значение"
    assert data["company_id"] == 1, "Поле 'company_id' содержит неверное значение"
    assert isinstance(
        data["created_at"], str
    ), "Поле 'created_at' должно быть строкой (ISO формат)"
