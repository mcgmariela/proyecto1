# Generated by Django 3.0.1 on 2022-05-01 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0009_auto_20220501_0023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posteos',
            name='imagen_post',
        ),
    ]
