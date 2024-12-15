# Generated by Django 5.1.4 on 2024-12-15 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="author",
            options={
                "ordering": ["last_name", "first_name"],
                "verbose_name": "Автор",
                "verbose_name_plural": "Авторы",
            },
        ),
        migrations.AlterModelOptions(
            name="book",
            options={
                "ordering": ["title", "author"],
                "verbose_name": "Книга",
                "verbose_name_plural": "Книги",
            },
        ),
        migrations.AlterModelOptions(
            name="genre",
            options={"verbose_name": "Жанр", "verbose_name_plural": "Жанры"},
        ),
    ]
