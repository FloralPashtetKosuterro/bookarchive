from django.db import models

class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length = 25)
    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    def __str__(self):
        return self.category

class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    news_name = models.CharField(max_length = 50)
    news_time = models.DateField()
    news_contains = models.CharField(max_length = 365)
    news_image = models.ImageField(blank=True, null=True)
    class Meta():
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
    def __str__(self):
        return self.news_name