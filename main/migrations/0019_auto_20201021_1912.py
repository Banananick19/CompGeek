# Generated by Django 3.0.4 on 2020-10-21 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20201019_2355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='count',
            new_name='views',
        ),
    ]
