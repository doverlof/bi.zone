# myapp/urls.py
from django.urls import path
from .views import (
    SubnetDeleteView,
    SubnetFilterView,
    SubnetListView,
    SubnetCreateView,
)

urlpatterns = [
    path("subnet/", SubnetListView.as_view(), name="subnet_list"),
    path("create/", SubnetCreateView.as_view(), name="subnet_create"),
    path("delete/<int:pk>/", SubnetDeleteView.as_view(), name="subnet_delete"),
    path(
        "filter/",
        SubnetFilterView.as_view(),
        name="filtеr",
    ),
]
