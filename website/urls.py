from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from .views import (
    home,
    )

urlpatterns = [
    path('', home, name="website_home"),
]
