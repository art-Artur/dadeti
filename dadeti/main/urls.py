from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("book", views.book, name="book"),
    path("article", views.article, name="article"),
    path("journal", views.journal, name="journal"),
]