# Generated by Django 4.2.1 on 2023-09-14 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_aksiyodorlar_category_aksiyodorlar_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoy',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
