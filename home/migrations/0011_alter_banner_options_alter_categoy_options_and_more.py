# Generated by Django 4.2.1 on 2023-08-05 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_categoy_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': 'Banner', 'verbose_name_plural': 'Bannerlar'},
        ),
        migrations.AlterModelOptions(
            name='categoy',
            options={'verbose_name': 'Asosiy Kategoriya', 'verbose_name_plural': 'Asosiy Kategoriyalar'},
        ),
        migrations.AddField(
            model_name='banner',
            name='desc_uz',
            field=models.CharField(max_length=232, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='name_uz',
            field=models.CharField(max_length=232, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='title_uz',
            field=models.CharField(max_length=232, null=True),
        ),
        migrations.AddField(
            model_name='categoy',
            name='name_uz',
            field=models.CharField(max_length=232, null=True),
        ),
        migrations.AddField(
            model_name='ishlabchiqrish',
            name='desc_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='ishlabchiqrish',
            name='title_uz',
            field=models.CharField(max_length=232, null=True),
        ),
        migrations.AddField(
            model_name='jarayon',
            name='desc_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='jarayon',
            name='title_uz',
            field=models.CharField(max_length=232, null=True),
        ),
        migrations.AddField(
            model_name='sidecategory',
            name='name_uz',
            field=models.CharField(max_length=232, null=True),
        ),
        migrations.AddField(
            model_name='tanishuv',
            name='desc_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='tanishuv',
            name='title_uz',
            field=models.CharField(max_length=232, null=True),
        ),
    ]