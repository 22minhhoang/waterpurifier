from django.contrib import admin

from waterpurifier.delivery.models import Customer, Device, Order

# Register your models here.
admin.site.register(Customer)
admin.site.register(Device)
admin.site.register(Order)
