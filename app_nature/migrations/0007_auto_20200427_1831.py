# Generated by Django 2.2.1 on 2020-04-27 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_nature', '0006_auto_20200427_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_nature.Profile'),
        ),
    ]
