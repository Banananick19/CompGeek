# Generated by Django 3.0.4 on 2020-09-28 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_article_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='views',
        ),
    ]
