from django.views.generic import CreateView
from django.urls import reverse_lazy

from users.form import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('catalog:index')
    template_name = 'users/signup.html'
