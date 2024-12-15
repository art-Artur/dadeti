from django.contrib import admin
from .models import Genre
from .models import Book
from .models import Author
# Register your models here.

admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Author)

#peakyblinders