from faker import Faker
import factory
from datetime import datetime
from myapp.models import Subnet

fake = Faker()


class SubnetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Subnet

    # Генерация уникального IP-адреса с подсетью
    subnet = factory.LazyFunction(lambda: f"{fake.ipv4_private()}/24")
    company_id = factory.Sequence(lambda n: n + 1)  # Инкрементируемый ID компании
