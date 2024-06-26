from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
import datetime
from django.utils import timezone


def default_time():
    return timezone.now() + timezone.timedelta(hours=3)


class User(AbstractUser):
    photo = models.ImageField(default="profile_img.png" ,blank=True, null=True)
    blocked_reason = models.TextField(blank=True, null=True)
    is_blocked = models.BooleanField(default=False)

class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=25)

    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.category


class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    news_name = models.CharField(max_length=50)
    news_time = models.DateField()
    news_contains = models.CharField(max_length=365)
    news_image = models.ImageField(blank=True, null=True)

    class Meta():
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.news_name


class Genres(models.Model):
    id = models.BigAutoField(primary_key=True)
    genre_name = models.TextField()

    class Meta():
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.genre_name


class Status(models.Model):
    status_name = models.TextField()

    class Meta():
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return self.status_name


class Books(models.Model):
    id = models.BigAutoField(primary_key=True)
    book_name = models.CharField(max_length=50)
    book_img = models.ImageField(blank=True, null=True, default=None)
    book_description = models.CharField(max_length=255)
    books_time = models.DateField(default=datetime.datetime.now())
    book_status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True)
    genres = models.ManyToManyField(Genres, related_name='books')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)

    class Meta():
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.book_name


class Rating(models.Model):
    id = models.BigAutoField(primary_key=True)
    rating_value = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(1)])
    book = models.ForeignKey(Books, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)

    class Meta():
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

    def __str__(self):
        return f'Оценка: {self.rating_value},' + f' Пользователь: {self.user}'


class Parts(models.Model):
    id = models.BigAutoField(primary_key=True)
    part_name = models.TextField()
    created_at = models.DateField(default=datetime.datetime.now())
    part_content = RichTextField(blank=True, null=True)
    book = models.ForeignKey(Books, related_name='parts', on_delete=models.CASCADE, null=True)

    class Meta():
        verbose_name = "Глава"
        verbose_name_plural = "Главы"

    def __str__(self):
        return self.part_name


class Comments(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment_text = RichTextField(blank=True, null=True)
    comment_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    part = models.ForeignKey(Parts, on_delete=models.CASCADE, blank=True, null=True)
    comment_date = models.DateTimeField(default=default_time)

    class Meta():
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.comment_text + str(self.comment_author)


class Reports(models.Model):
    id = models.BigAutoField(primary_key=True)
    report_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    report_theme = models.CharField(max_length=40)
    report_content = models.CharField(max_length=255, blank=True, null=True)
    comment = models.ForeignKey(Comments, default=None, on_delete=models.CASCADE, blank=True, null=True)
    book = models.ForeignKey(Books, default=None, on_delete=models.CASCADE, blank=True, null=True)
    status = models.BooleanField(default=False,blank=True, null=True)
    decision = models.BooleanField(default=False,blank=True, null=True)

    class Meta():
        verbose_name = "Жалоба"
        verbose_name_plural = "Жалобы"

    def __str__(self):
        return self.report_theme
