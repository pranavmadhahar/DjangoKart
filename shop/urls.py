from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="About"),
    path("contact/", views.contact, name="Contact"),
    path("tracker/", views.tracker, name="tracker"),
    path("search/", views.search, name="search"),
    path("products/<int:product_id>/", views.productview, name="productview"),
    path("checkout/", views.checkout, name="checkout"),
]