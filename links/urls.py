from django.urls import path

from . import views

urlpatterns = [
    path("", views.links, name="links")
]
