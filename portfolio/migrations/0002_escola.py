# Generated by Django 4.0.4 on 2022-05-25 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('periodo', models.CharField(max_length=50)),
                ('local', models.CharField(max_length=200)),
            ],
        ),
    ]