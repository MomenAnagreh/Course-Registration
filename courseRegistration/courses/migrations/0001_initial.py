# Generated by Django 4.0.4 on 2022-04-16 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('time', models.TextField()),
                ('day', models.CharField(max_length=100)),
                ('instructor', models.CharField(max_length=100)),
            ],
        ),
    ]
