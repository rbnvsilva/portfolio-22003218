# Generated by Django 4.0.4 on 2022-05-26 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_escola_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='escola',
            name='image',
        ),
    ]
