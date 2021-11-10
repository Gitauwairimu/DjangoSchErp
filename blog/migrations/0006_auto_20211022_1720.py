# Generated by Django 3.2.4 on 2021-10-22 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20211021_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='female', max_length=20),
        ),
    ]
