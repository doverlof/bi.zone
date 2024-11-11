from time import timezone
import factory
from datetime import datetime
from myapp.models import Subnet


class SubnetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Subnet

    subnet = "192.168.1.0/24"
    company_id = 1
