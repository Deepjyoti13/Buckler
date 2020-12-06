from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("tracker/", views.tracker, name="tracker"),
    path("search/", views.search, name="search"),
    path("productView/", views.productView, name="productView"),
    path("checkOut/", views.checkOut, name="checkOut"),
]
