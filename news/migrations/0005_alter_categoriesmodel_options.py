# Generated by Django 3.2.4 on 2021-06-16 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210616_0958'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriesmodel',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]