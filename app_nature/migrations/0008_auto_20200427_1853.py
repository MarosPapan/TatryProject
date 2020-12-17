# Generated by Django 2.2.1 on 2020-04-27 16:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_nature', '0007_auto_20200427_1831'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='user',
            new_name='author',
        ),
        migrations.AddField(
            model_name='posts',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
