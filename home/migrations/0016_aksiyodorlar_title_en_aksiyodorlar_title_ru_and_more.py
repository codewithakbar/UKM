# Generated by Django 4.2.1 on 2023-08-10 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_aksiyodorlar'),
    ]

    operations = [
        migrations.AddField(
            model_name='aksiyodorlar',
            name='title_en',
            field=models.CharField(max_length=232, null=True),
        ),
        migrations.AddField(
            model_name='aksiyodorlar',
            name='title_ru',
            field=models.CharField(max_length=232, null=True),
        ),
        migrations.AddField(
            model_name='aksiyodorlar',
            name='title_uz',
            field=models.CharField(max_length=232, null=True),
        ),
    ]
