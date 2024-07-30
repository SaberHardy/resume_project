# Generated by Django 4.2.14 on 2024-07-30 04:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0002_alter_aboutme_about_me'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]
