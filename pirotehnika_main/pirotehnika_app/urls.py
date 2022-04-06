from django.urls import path

from .views import *
urlpatterns = [
    path("", ProductsView.as_view(), name="home"),
    path('catalog/', ProductsViewCatalog.as_view(), name='catalog'),

    path('products/<str:product_slug>/',
         ProductDetailViewCatalog.as_view(), name='catalog_detail'),

    path('contact/', contact, name='contact'),
    path('dostavka/', dostavka, name='dostavka'),
    path('login/', LoginUser.as_view(), name='login'),
    path('registration/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('products/<str:product_slug>/',
         ProductDetailView.as_view(), name='product_detail'),

]
