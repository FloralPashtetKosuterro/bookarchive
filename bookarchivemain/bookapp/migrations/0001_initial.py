# Generated by Django 5.0.1 on 2024-02-13 10:44

import ckeditor.fields
import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('genre_name', models.TextField()),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('news_name', models.CharField(max_length=50)),
                ('news_time', models.DateField()),
                ('news_contains', models.CharField(max_length=365)),
                ('news_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.TextField()),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=50)),
                ('book_img', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('book_description', models.CharField(max_length=255)),
                ('books_time', models.DateField(default=datetime.datetime(2024, 2, 13, 13, 44, 44, 623667))),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('genres', models.ManyToManyField(related_name='books', to='bookapp.genres')),
                ('book_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookapp.status')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('part_name', models.TextField()),
                ('part_content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='bookapp.books')),
            ],
            options={
                'verbose_name': 'Глава',
                'verbose_name_plural': 'Главы',
            },
        ),
    ]
