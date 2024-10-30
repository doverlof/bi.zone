# myapp/views.py
from rest_framework import generics
from .models import Subnet
from .serializers import SubnetSerializer
from django.utils.dateparse import parse_datetime


class SubnetListView(generics.ListAPIView):
    queryset = Subnet.objects.all()
    serializer_class = SubnetSerializer


class SubnetCreateView(generics.CreateAPIView):
    queryset = Subnet.objects.all()
    serializer_class = SubnetSerializer


class SubnetDeleteView(generics.DestroyAPIView):
    queryset = Subnet.objects.all()
    serializer_class = SubnetSerializer


class SubnetFilterView(generics.ListAPIView):
    serializer_class = SubnetSerializer

    def get_queryset(self):
        queryset = Subnet.objects.all()

        company_id_param = self.request.query_params.get("company_id")
        if company_id_param:
            queryset = queryset.filter(company_id=company_id_param)

        subnet_param = self.request.query_params.get("subnet")
        if subnet_param:
            queryset = queryset.filter(subnet=subnet_param)

        id_param = self.request.query_params.get("id")
        if id_param:
            queryset = queryset.filter(id=id_param)

        before_date_param = self.request.query_params.get("before_date")
        after_date_param = self.request.query_params.get("after_date")

        if before_date_param:
            before_date = parse_datetime(before_date_param)
            if before_date:
                queryset = queryset.filter(created_at__lte=before_date)

        if after_date_param:
            after_date = parse_datetime(after_date_param)
            if after_date:
                queryset = queryset.filter(created_at__gte=after_date)

        return queryset
