from django.shortcuts import render
from .models import Book, Author, Genre
from django.views import generic

# Create your views here.

def index(request):
    return render(request, "main/index.html")

def article(request):
    return render(request, "main/article.html")

def journal(request):
    return render(request, "main/journal.html")

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Book

class AuthorDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Author