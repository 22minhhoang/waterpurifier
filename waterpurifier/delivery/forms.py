from django import forms
from django.contrib.auth import get_user_model

from waterpurifier.delivery.models import Customer, Device, Order

User = get_user_model()


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        widgets = {
            "email": forms.EmailInput(),
            "birth_date": forms.DateInput(attrs={"type": "date"}),
        }


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = "__all__"
        widgets = {
            "year_of_manufacture": forms.DateInput(attrs={"type": "date"}),
            "comment": forms.Textarea(),
        }


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        # Create Order from Customer
        if "customer" in self.initial:
            self.fields["customer"].queryset = Customer.objects.filter(
                pk=self.initial["customer"]
            )
        self.fields["staff"].queryset = User.objects.filter(is_superuser=False)

    class Meta:
        model = Order
        fields = "__all__"
        exclude = ["updated_date"]
        widgets = {
            "delivery_date": forms.DateInput(attrs={"type": "date"}),
            "comment": forms.Textarea(),
        }
