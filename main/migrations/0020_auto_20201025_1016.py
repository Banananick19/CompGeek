# Generated by Django 3.0.4 on 2020-10-25 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20201021_1912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='primarycategory',
            old_name='slug',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='secondarycategory',
            old_name='slug',
            new_name='tag',
        ),
    ]
