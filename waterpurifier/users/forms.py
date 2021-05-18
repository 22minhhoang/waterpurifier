from allauth.account.forms import SignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.forms import CharField, DateInput, EmailInput, ModelForm
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserChangeAdminForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationAdminForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ["name", "phone_number", "email", "address"]
        widgets = {
            "email": EmailInput(),
            "birth_date": DateInput(attrs={"type": "date"}),
        }


# class UserSignUpForm(SignupForm):
#     class Meta:
#         exclude = ["email"]

#     def save(self, request):

#         # Ensure you call the parent class's save.
#         # .save() returns a User object.
#         user = super(UserSignUpForm, self).save(request)

#         # Add your own processing here.

#         # You must return the original result.
#         return user
