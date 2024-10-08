# Generated by Django 5.0.7 on 2024-07-25 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home1', '0007_courseregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('tenth_marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('twelfth_marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('diploma_marks', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('competitive_exam_score', models.DecimalField(decimal_places=2, max_digits=8)),
                ('university_exam_score', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('course', models.CharField(max_length=100)),
            ],
        ),
    ]
