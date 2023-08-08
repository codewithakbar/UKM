# Generated by Django 4.2.1 on 2023-08-08 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_categoy_slug_alter_jarayon_desc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoy',
            name='slug_en',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='categoy',
            name='slug_ru',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='categoy',
            name='slug_uz',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
