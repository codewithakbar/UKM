# Generated by Django 4.2.1 on 2023-09-14 04:48

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yangiliklar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=233)),
                ('title_uz', models.CharField(max_length=233, null=True)),
                ('title_en', models.CharField(max_length=233, null=True)),
                ('title_ru', models.CharField(max_length=233, null=True)),
                ('desc', ckeditor.fields.RichTextField()),
                ('desc_uz', ckeditor.fields.RichTextField(null=True)),
                ('desc_en', ckeditor.fields.RichTextField(null=True)),
                ('desc_ru', ckeditor.fields.RichTextField(null=True)),
                ('image', models.ImageField(upload_to='news/%Y/%m/%d')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='yangilik', to='news.yangiliklar')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
