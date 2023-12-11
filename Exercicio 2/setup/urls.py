from django.contrib import admin
from django.urls import path
from cloudPark.views import homeView

urlpatterns = [
    path("", homeView.as_view(), name="home"),
]
