from django.db import models

# Create your models here.
class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length = 25)
    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    def __str__(self):
        return self.category