from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.functions import Upper
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from waterpurifier.users.forms import UserUpdateForm

User = get_user_model()


class UserListView(LoginRequiredMixin, ListView):
    paginate_by = 20
    model = User
    queryset = User.objects.filter(is_superuser=False).order_by(Upper("name"))
    context_object_name = "users"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Nhân viên"

        return context


user_list_view = UserListView.as_view()


class UserDetailView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    # slug_field = "username"
    # slug_url_kwarg = "username"

    def get_object(self):
        return self.request.user


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_message = _("Information successfully updated")

    def get_success_url(self):
        return self.request.user.get_absolute_url()  # type: ignore [union-attr]

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()
