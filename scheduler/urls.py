from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("users/", views.users, name="users"),
    path("datetimes/", views.datetimes, name="datetimes"),
]