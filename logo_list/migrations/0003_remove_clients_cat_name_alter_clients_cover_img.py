# Generated by Django 4.1.7 on 2023-02-25 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logo_list', '0002_clients_cat_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='cat_name',
        ),
        migrations.AlterField(
            model_name='clients',
            name='cover_img',
            field=models.ImageField(blank=True, null=True, upload_to='clients'),
        ),
    ]
