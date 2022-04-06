from django import views
from django.shortcuts import get_object_or_404, redirect, render
from .forms import AddOrderForm
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Dostavka
from django.contrib.auth import login, logout
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .forms import LoginUserForm


class ProductsView(views.View):
    def get(self, request, **kwargs):
        products = CategoryProducts.objects.all()
        context = {
            'products': products,
        }

        return render(request, 'home.html', context)


class ProductsViewCatalog(views.View):
    def get(self, request, **kwargs):
        products = CategoryProducts.objects.all()
        context = {
            'products': products,
        }

        return render(request, 'catalog.html', context)


class ProductDetailViewCatalog(views.generic.DetailView, LoginRequiredMixin, CreateView):

    model = CategoryProducts
    template_name = 'catalog_detail.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    form_class = AddOrderForm
    template_name = 'catalog_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return dict(list(context.items()) + list())

    def get_success_url(self):
        return reverse_lazy('home')


class ProductDetailView(views.generic.DetailView, LoginRequiredMixin, CreateView):

    model = CategoryProducts
    template_name = 'product_detail.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    form_class = AddOrderForm
    template_name = 'product_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return dict(list(context.items()) + list())

    def get_success_url(self):
        return reverse_lazy('home')


def katalog(request):
    return render(request, 'katalog.html', {'header': 'katalog'})


def contact(request):
    return render(request, 'contact.html', {'header': 'contact'})


def dostavka(request):
    dostavka = Dostavka.objects.all()
    return render(request, 'dostavka.html', {'dostavka': dostavka, 'header': 'dostavka'})


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
