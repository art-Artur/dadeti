from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

class Genre(models.Model):
    """Модель жанра книги"""
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Введите жанр книги"
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular genre instance."""
        return reverse('genre-detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message = "Такой жанр уже есть (чувствительно к регистру)"
            ),
        ]

class Book(models.Model):
    """
    Модель книги
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    description = models.TextField(max_length=1000, help_text="Введите краткое описание книги")
    genre = models.ManyToManyField(Genre, help_text="Выберите жанр книги")
    year = models.DateField(null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    book_text = models.TextField()
    popularity = models.SmallIntegerField(help_text="Введите рейтинг популярности от 1 до 10")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['title', 'author']

    def display_genre(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'

    def get_absolute_url(self):
        """Returns the url to access a particular book record."""
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Author(models.Model):
    """
    Модель автора
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    biography = models.TextField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

