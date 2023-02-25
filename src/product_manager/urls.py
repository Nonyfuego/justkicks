from django.urls import path
from . import views

urlpatterns = [
    path("api/v1/products/", views.get_all_products)
]