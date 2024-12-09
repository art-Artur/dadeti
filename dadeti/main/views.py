from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def book(request):
    return render(request, "main/book.html")

def article(request):
    return render(request, "main/article.html")

def journal(request):
    return render(request, "main/journal.html")