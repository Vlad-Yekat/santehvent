from django.shortcuts import render

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterView(CreateView):
    template_name = "user/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('catalog:index')
