# Generated by Django 5.0.7 on 2024-07-25 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home1', '0017_leave'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leave',
            name='duration',
        ),
    ]
