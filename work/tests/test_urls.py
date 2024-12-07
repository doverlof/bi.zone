from django.urls import reverse, resolve
from myapp.views import (
    SubnetListView,
    SubnetCreateView,
    SubnetDeleteView,
    SubnetFilterView,
)


def test_subnet_list_url():
    path = reverse("subnet_list")
    assert path == "/subnet/"
    assert resolve(path).func.view_class == SubnetListView


def test_subnet_create_url():
    path = reverse("subnet_create")
    assert path == "/create/"
    assert resolve(path).func.view_class == SubnetCreateView


def test_subnet_delete_url():
    path = reverse("subnet_delete", kwargs={"pk": 1})
    assert path == "/delete/1/"
    assert resolve(path).func.view_class == SubnetDeleteView


def test_subnet_filter_url():
    path = reverse("filter")
    assert path == "/filter/"
    assert resolve(path).func.view_class == SubnetFilterView
