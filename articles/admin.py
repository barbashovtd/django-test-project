from django.contrib import admin

from .models import Article, Author


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "text",
        "creator",
        "rate",
        "views",
    )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = (
        "nickname",
        "email",
        "articles",
    )


# python manage.py makemigrations
