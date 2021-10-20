from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry, name="entry"),
    path("create/post", views.create, name="create"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("random/", views.random_page, name="random"),
]
