# Generated by Django 5.0.1 on 2024-01-30 17:00

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0008_parts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parts',
            name='part_content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]