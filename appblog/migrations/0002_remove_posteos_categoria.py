# Generated by Django 3.0.1 on 2022-03-30 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posteos',
            name='categoria',
        ),
    ]
