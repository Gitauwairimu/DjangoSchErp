# Generated by Django 3.2.4 on 2021-10-31 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0043_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
