from django.shortcuts import get_object_or_404, redirect, render

from .forms import *

from .models import Dostavka
from django.contrib.auth import login, logout
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .forms import LoginUserForm


def home(request):
    return render(request, 'home.html', {'header': 'home'})


def katalog(request):
    return render(request, 'katalog.html', {'header': 'katalog'})


def contact(request):
    return render(request, 'contact.html', {'header': 'contact'})


def dostavka(request):
    dostavka = Dostavka.objects.all()
    return render(request, 'dostavka.html', {'dostavka': dostavka, 'header': 'dostavka'})


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()

#             return redirect('login')
#     else:
#         form = UserRegistrationForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'register.html', context)


# Create your views here.

class RegisterUser(CreateView):

    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        content = {'header': 'register'}
        context = super().get_context_data(**kwargs)

        return dict(list(context.items()) + list())

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return dict(list(context.items()) + list())

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):

    logout(request)
    return redirect('login')
