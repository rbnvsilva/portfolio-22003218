# Generated by Django 4.0.4 on 2022-05-25 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_interesse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=50)),
                ('data', models.DateField()),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField(max_length=500)),
                ('link', models.CharField(max_length=300)),
            ],
        ),
    ]
