from django.urls import path
from pirotehnika_app import views
from .views import *
from django.conf.urls import url
urlpatterns = [
    path("", views.home, name="home"),
    path('katalog/', views.katalog, name='katalog'),
    path('contact/', views.contact, name='contact'),
    path('dostavka/', views.dostavka, name='dostavka'),
    path('login/', LoginUser.as_view(), name='login'),
    path('registration/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),

]
