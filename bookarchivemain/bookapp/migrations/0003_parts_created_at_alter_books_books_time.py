# Generated by Django 4.2.10 on 2024-06-23 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0002_alter_books_books_time_alter_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='parts',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2024, 6, 23, 9, 21, 0, 233595)),
        ),
        migrations.AlterField(
            model_name='books',
            name='books_time',
            field=models.DateField(default=datetime.datetime(2024, 6, 23, 9, 21, 0, 231286)),
        ),
    ]
