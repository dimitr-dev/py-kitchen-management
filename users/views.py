from django.urls import reverse_lazy
from django.views import generic

from users.forms import CookCreationForm


class CookSignUpView(generic.CreateView):
    form_class = CookCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
