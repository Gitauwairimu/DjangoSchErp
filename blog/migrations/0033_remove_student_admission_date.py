# Generated by Django 3.2.4 on 2021-10-29 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20211029_0741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='admission_date',
        ),
    ]
