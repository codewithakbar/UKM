# Generated by Django 4.2.1 on 2023-06-24 09:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_banner_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='desc',
            field=models.CharField(default='', max_length=232),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='banner',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=232),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='SideCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=232)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='home.sidecategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Categoy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=232)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='home.categoy')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
