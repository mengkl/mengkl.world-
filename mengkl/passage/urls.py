from django.urls import path

from . import views

urlpatterns = [
    path("<int:pid>/", views.passage_show, name="passage_show"),
    path("", views.passage_index, name="passage_index"),
]
