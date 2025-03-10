# Generated by Django 5.1.4 on 2024-12-15 19:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_alter_book_book_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="biography",
            field=models.TextField(
                blank=True, max_length=1000, null=True, verbose_name="Биография"
            ),
        ),
        migrations.AlterField(
            model_name="author",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True, verbose_name="Дата рождения"),
        ),
        migrations.AlterField(
            model_name="author",
            name="date_of_death",
            field=models.DateField(blank=True, null=True, verbose_name="Дата смерти"),
        ),
        migrations.AlterField(
            model_name="author",
            name="first_name",
            field=models.CharField(max_length=100, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="author",
            name="last_name",
            field=models.CharField(max_length=100, verbose_name="Фамилия"),
        ),
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="main.author",
                verbose_name="Автор",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="description",
            field=models.TextField(
                help_text="Введите краткое описание книги",
                max_length=1000,
                verbose_name="Описание",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="genre",
            field=models.ManyToManyField(
                help_text="Выберите жанр книги", to="main.genre", verbose_name="Жанр"
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="image",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Картинка"
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="popularity",
            field=models.SmallIntegerField(
                help_text="Введите рейтинг популярности от 1 до 10",
                verbose_name="Популярность",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.CharField(max_length=200, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="book",
            name="year",
            field=models.DateField(
                blank=True, null=True, verbose_name="Дата написания"
            ),
        ),
        migrations.AlterField(
            model_name="genre",
            name="name",
            field=models.CharField(
                help_text="Введите жанр книги",
                max_length=200,
                unique=True,
                verbose_name="Название",
            ),
        ),
    ]
