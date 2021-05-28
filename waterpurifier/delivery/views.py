from datetime import date, timedelta

from django.contrib import messages

# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import add_message
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.functions import Upper
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from waterpurifier.delivery.forms import CustomerForm, DeviceForm, OrderForm
from waterpurifier.delivery.models import Customer, Device, Order


# Create your views here.
def home(request):
    today = date.today()
    limit = today + timedelta(weeks=1)
    # for order in Order.objects.filter(delivery_date__gte=today).filter(delivery_date__lte=limit).order_by('delivery_date'):
    orders = (
        Order.objects.filter(delivery_date__gte=today, delivery_date__lte=limit)
        .exclude(completed__exact="F")
        .order_by("delivery_date")
    )
    if orders:
        for order in orders:
            gen = "ông"
            if order.customer.gender == "F":
                gen = "bà"
            mesType = messages.INFO
            if order.delivery_date == today:
                mesType = messages.WARNING
            add_message(
                request,
                mesType,
                f"[{order.delivery_date:%d/%m/%Y}] {gen} {order.customer}: {order.device}",
            )
    else:
        add_message(request, messages.INFO, "Hiện tại không có thông báo nào")

    return render(request, "delivery/home.html")


class CustomerListView(ListView):
    # model = Customer
    paginate_by = 20
    queryset = Customer.objects.order_by(Upper("name"))
    context_object_name = "customers"
    template_name = "delivery/list.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context["type"] = "customer"
        context["page_title"] = "Khách hàng"
        context["create_url"] = "delivery:customer-create"
        context["update_url"] = "delivery:customer-update"
        return context


class CustomerCreateView(SuccessMessageMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "delivery/create.html"
    success_url = reverse_lazy("delivery:customer-list")
    success_message = "Đã thêm khách hàng '%(name)s' thành công!"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context["page_title"] = "Khách hàng"
        context["back_url"] = "delivery:customer-list"
        return context


class CustomerUpdateView(SuccessMessageMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "delivery/update.html"
    # success_url = reverse_lazy('delivery:customer-list')
    success_message = "Đã cập nhật khách hàng '%(name)s' thành công!"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context["page_title"] = "Khách hàng"
        context["back_url"] = "delivery:customer-list"
        context["delete_url"] = "delivery:customer-delete"
        context["add_order_url"] = "delivery:customer-addorder"
        return context


class CustomerDeleteView(SuccessMessageMixin, DeleteView):
    model = Customer
    form_class = CustomerForm
    template_name = "delivery/delete.html"
    success_url = reverse_lazy("delivery:customer-list")
    success_message = "Đã xóa khách hàng thành công!"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context["page_title"] = "Khách hàng"
        context["back_url"] = "delivery:customer-list"
        return context


class AddOrderView(SuccessMessageMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = "delivery/create.html"
    success_url = reverse_lazy("delivery:order-list")
    success_message = "Đã thêm order thành công!"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        customer = Customer.objects.get(pk=self.kwargs["pk"])
        context["form"] = OrderForm(initial={"customer": customer.pk})
        context["page_title"] = "Đơn đặt hàng"
        context["back_url"] = "delivery:customer-list"
        return context


class DeviceListView(ListView):
    context_object_name = "devices"
    queryset = Device.objects.order_by(Upper("name"))
    paginate_by = 20
    template_name = "delivery/list.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context["type"] = "device"
        context["page_title"] = "Thiết bị"
        context["create_url"] = "delivery:device-create"
        context["update_url"] = "delivery:device-update"
        return context


class DeviceCreateView(SuccessMessageMixin, CreateView):
    model = Device
    form_class = DeviceForm
    template_name = "delivery/create.html"
    success_url = reverse_lazy("delivery:device-list")
    success_message = "Đã thêm thiết bị '%(name)s' thành công!"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context["page_title"] = "Thiết bị"
        context["back_url"] = "delivery:device-list"
        return context


class DeviceUpdateView(SuccessMessageMixin, UpdateView):
    model = Device
    form_class = DeviceForm
    template_name = "delivery/update.html"
    # success_url = reverse_lazy('delivery:device-list')
    success_message = "Đã cập nhật thiết bị '%(name)s' thành công!"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context["page_title"] = "Thiết bị"
        context["back_url"] = "delivery:device-list"
        context["delete_url"] = "delivery:device-delete"
        return context


class DeviceDeleteView(SuccessMessageMixin, DeleteView):
    model = Device
    form_class = DeviceForm
    template_name = "delivery/delete.html"
    success_url = reverse_lazy("delivery:device-list")
    success_message = "Đã xóa thiết bị '%(name)s' thành công!"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context["page_title"] = "Thiết bị"
        context["back_url"] = "delivery:device-list"
        return context


class OrderListView(ListView):
    # model = Order
    context_object_name = "orders"
    queryset = Order.objects.order_by("-delivery_date")
    paginate_by = 20
    template_name = "delivery/list.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["type"] = "order"
        context["page_title"] = "Đơn hàng"
        context["create_url"] = "delivery:order-create"
        context["update_url"] = "delivery:order-update"
        return context


class OrderUpdateView(SuccessMessageMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "delivery/update.html"
    # success_url = reverse_lazy('delivery:staff-list')
    success_message = "Đã cập nhật order thành công!"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context["page_title"] = "Đơn đặt hàng"
        context["back_url"] = "delivery:order-list"
        context["delete_url"] = "delivery:order-delete"
        return context


class OrderDeleteView(SuccessMessageMixin, DeleteView):
    model = Order
    form_class = OrderForm
    template_name = "delivery/delete.html"
    success_url = reverse_lazy("delivery:order-list")
    success_message = "Đã xóa order thành công!"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context["page_title"] = "Đơn đặt hàng"
        context["back_url"] = "delivery:order-list"
        return context
