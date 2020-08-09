from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from . import forms


class IndexView(TemplateView):
    template_name = 'index.html'


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = forms.RegisterUserForm
    success_url = ''

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('')

    def form_invalid(self, form):
        pass


# @login_required
class DashboardView(TemplateView):
    template_name = 'home.html'
