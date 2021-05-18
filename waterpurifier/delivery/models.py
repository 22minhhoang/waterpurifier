from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    GENDERS = (("M", "Ông"), ("F", "Bà"))
    gender = models.CharField(max_length=1, choices=GENDERS)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("delivery:customer-update", kwargs={"pk": self.pk})


class Device(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=50, null=True, blank=True)
    year_of_manufacture = models.DateField(
        null=True,
        blank=True,
    )
    comment = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("delivery:device-update", kwargs={"pk": self.pk})


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    delivery_date = models.DateField()
    updated_date = models.DateTimeField(
        auto_now=True,
    )
    STATUS = (("P", "Chưa hoàn thành"), ("F", "Hoàn thành"))
    completed = models.CharField(max_length=1, choices=STATUS, default="P")
    comment = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return "[%s] %s - %s" % (self.updated_date, self.customer, self.device)

    def get_absolute_url(self):
        return reverse("delivery:order-update", kwargs={"pk": self.pk})
