# Generated by Django 5.0.1 on 2024-05-04 17:24

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0005_alter_books_books_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='part',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookapp.parts'),
        ),
        migrations.AlterField(
            model_name='books',
            name='books_time',
            field=models.DateField(default=datetime.datetime(2024, 5, 4, 20, 24, 9, 587427)),
        ),
    ]