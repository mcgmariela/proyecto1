# Generated by Django 3.0.1 on 2022-05-01 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0007_auto_20220501_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='posteos',
            name='encabezado_imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
