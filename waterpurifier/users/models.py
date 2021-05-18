from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for WaterPurifier."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Tên nhân viên"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    GENDERS = (("M", "Ông"), ("F", "Bà"))
    gender = CharField(max_length=1, choices=GENDERS)
    birth_date = DateField(null=True, blank=True)
    phone_number = CharField(max_length=20, null=True, blank=True)
    address = CharField(max_length=200, null=True, blank=True)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
