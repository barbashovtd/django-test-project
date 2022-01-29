from django.db import models


class Author(models.Model):
    nickname = models.CharField("Ник", max_length=32)
    email = models.EmailField("Почта")
    articles = models.ForeignKey("Article", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.nickname}  ({self.email})"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Article(models.Model):
    title = models.CharField("Название", max_length=64)
    text = models.TextField("Текст статьи")
    views = models.PositiveIntegerField("Просмотры", default=0)
    rate = models.IntegerField("Оценка", default=0)
    creator = models.ForeignKey(
        Author, verbose_name="Автор", on_delete=models.DO_NOTHING
    )
    engage_image = models.ImageField(
        "КДПВ",
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now=True)
    # comments =

    def __str__(self):
        return f"{self.title}  ({self.creator})"

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
