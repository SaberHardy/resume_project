# Generated by Django 4.2.14 on 2024-07-26 04:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='about_me',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
