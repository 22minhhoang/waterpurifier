from django.urls import path

from waterpurifier.delivery.views import (
    AddOrderView,
    CustomerCreateView,
    CustomerDeleteView,
    CustomerListView,
    CustomerUpdateView,
    DeviceCreateView,
    DeviceDeleteView,
    DeviceListView,
    DeviceUpdateView,
    OrderDeleteView,
    OrderListView,
    OrderUpdateView,
    home,
)

app_name = "delivery"
urlpatterns = [
    path("", home, name="home"),
    path("customers/", CustomerListView.as_view(), name="customer-list"),
    path("customers/create/", CustomerCreateView.as_view(), name="customer-create"),
    path("customers/<int:pk>/", CustomerUpdateView.as_view(), name="customer-update"),
    path(
        "customers/<int:pk>/delete/",
        CustomerDeleteView.as_view(),
        name="customer-delete",
    ),
    path(
        "customers/<int:pk>/addorder/", AddOrderView.as_view(), name="customer-addorder"
    ),
    path("devices/", DeviceListView.as_view(), name="device-list"),
    path("devices/create/", DeviceCreateView.as_view(), name="device-create"),
    path("devices/<int:pk>/", DeviceUpdateView.as_view(), name="device-update"),
    path("devices/<int:pk>/delete/", DeviceDeleteView.as_view(), name="device-delete"),
    path("orders/", OrderListView.as_view(), name="order-list"),
    path("orders/<int:pk>/", OrderUpdateView.as_view(), name="order-update"),
    path("orders/<int:pk>/delete/", OrderDeleteView.as_view(), name="order-delete"),
]
