# Generated by Django 4.0.4 on 2022-04-18 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_thumb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='thumb',
        ),
    ]
