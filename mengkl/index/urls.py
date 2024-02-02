from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_page, {"page_id": "1"}),
    path("<int:page_id>/", views.index_page)
]
