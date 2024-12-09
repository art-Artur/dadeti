from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("book", views.book),
    path("article", views.article),
    path("journal", views.journal),
]