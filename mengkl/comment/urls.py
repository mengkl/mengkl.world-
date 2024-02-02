from django.urls import path

from . import views

urlpatterns = [
    path("<int:pid>/",views.comment_add, name='comment-add')
]
