from django.urls import path

from . import views

urlpatterns = [
    path("", views.search_index),
    path("tag/<str:tag_name>/", views.search_by_tag_name, name="search_by_tag"),
    path("search_from_passage/<str:tag_name>/", views.search_from_passage, name="search_from_passage"),
    path("<str:keyword>/", views.search_by_keyword, name="search_by_keyword"),
]
