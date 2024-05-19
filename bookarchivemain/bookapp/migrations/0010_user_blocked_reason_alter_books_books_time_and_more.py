# Generated by Django 5.0.1 on 2024-05-18 20:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0009_reports_status_alter_books_books_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='blocked_reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='books_time',
            field=models.DateField(default=datetime.datetime(2024, 5, 18, 23, 10, 49, 42487)),
        ),
        migrations.AlterField(
            model_name='reports',
            name='status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
