# myapp/urls.py
from django.urls import path
from .views import SubnetListView

urlpatterns = [
    path("", SubnetListView.as_view(), name="subnet_list"),
]
