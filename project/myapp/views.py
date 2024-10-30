# myapp/views.py
from rest_framework import generics
from .models import Subnet
from .serializers import SubnetSerializer


# Представление для отображения списка всех IP-подсетей
class SubnetListView(generics.ListAPIView):
    queryset = Subnet.objects.all()
    serializer_class = SubnetSerializer
