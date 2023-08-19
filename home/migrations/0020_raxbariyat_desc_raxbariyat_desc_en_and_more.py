# Generated by Django 4.2.1 on 2023-08-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_raxbariyat'),
    ]

    operations = [
        migrations.AddField(
            model_name='raxbariyat',
            name='desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='raxbariyat',
            name='desc_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='raxbariyat',
            name='desc_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='raxbariyat',
            name='desc_uz',
            field=models.TextField(null=True),
        ),
    ]
