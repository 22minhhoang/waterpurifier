from django.contrib.auth import get_user_model
from django.db.models import CASCADE, CharField, DateField, DateTimeField, ForeignKey, Model, SmallIntegerField
from django.urls import reverse

User = get_user_model()


# Create your models here.
class Customer(Model):
    name = CharField(max_length=100)
    GENDERS = (("M", "Ông"), ("F", "Bà"))
    gender = CharField(max_length=1, choices=GENDERS)
    birth_date = DateField(null=True, blank=True)
    phone_number = CharField(max_length=20, blank=True)
    PROVINCES = (
        (73, "Quảng Bình"),
        (74, "Quảng Trị"),
        (75, "Thừa Thiên Huế"),
        (43, "Đà Nẵng"),
        (92, "Quảng Nam"),
        (76, "Quảng Ngãi"),
        (0, "Khác"),
    )
    province = SmallIntegerField(choices=PROVINCES, blank=True)
    address_detail = CharField(max_length=200, blank=True)
    email = CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("delivery:customer-update", kwargs={"pk": self.pk})


class Device(Model):
    name = CharField(max_length=100)
    model_code = CharField(max_length=50, blank=True)
    year_of_manufacture = DateField(
        null=True,
        blank=True,
    )
    comment = CharField(max_length=200, blank=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("delivery:device-update", kwargs={"pk": self.pk})


class Component(Model):
    name = CharField(max_length=100)
    comment = CharField(max_length=200, blank=True)


class Order(Model):
    customer = ForeignKey(Customer, on_delete=CASCADE)
    device = ForeignKey(Device, on_delete=CASCADE, null=True, blank=True)
    staff = ForeignKey(User, on_delete=CASCADE, null=True, blank=True)
    delivery_date = DateField()
    updated_date = DateTimeField(
        auto_now=True,
    )
    STATUS = (("P", "Chưa hoàn thành"), ("F", "Hoàn thành"))
    completed = CharField(max_length=1, choices=STATUS, default="P")
    comment = CharField(max_length=200, blank=True)

    def __str__(self) -> str:
        return "[%s] %s - %s" % (self.updated_date, self.customer, self.device)

    def get_absolute_url(self):
        return reverse("delivery:order-update", kwargs={"pk": self.pk})
