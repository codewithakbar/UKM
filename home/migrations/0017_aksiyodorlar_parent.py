# Generated by Django 4.2.1 on 2023-08-10 05:15

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_aksiyodorlar_title_en_aksiyodorlar_title_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aksiyodorlar',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='home.aksiyodorlar'),
        ),
    ]