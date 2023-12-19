# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("home", views.index, name="index"),
    path("", views.redirect, name="index"),
    path("edit/<str:documento_id>/", views.room, name="documento"),
]