from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("book/", views.BookListView.as_view(), name="book"),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path("article", views.article, name="article"),
    path("journal", views.journal, name="journal"),
]