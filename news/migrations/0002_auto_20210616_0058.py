# Generated by Django 3.2.4 on 2021-06-15 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=250)),
                ('source', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
            },
        ),
        migrations.AlterField(
            model_name='categoriesmodel',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
