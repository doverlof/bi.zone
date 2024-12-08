import pytest
from django.db import IntegrityError
from myapp.models import Subnet


@pytest.mark.django_db
def test_duplicate_subnet_not_allowed():
    # Создаём первую запись
    Subnet.objects.create(subnet="192.168.1.0/24", company_id=1)

    # Пытаемся создать запись с таким же значением subnet
    with pytest.raises(IntegrityError) as excinfo:
        Subnet.objects.create(subnet="192.168.1.0/24", company_id=2)

    # Проверяем сообщение об ошибке
    assert "duplicate key value violates unique constraint" in str(excinfo.value)
