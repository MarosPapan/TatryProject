# Generated by Django 2.2.1 on 2020-04-28 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_nature', '0009_auto_20200428_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_nature.Profile'),
        ),
    ]
