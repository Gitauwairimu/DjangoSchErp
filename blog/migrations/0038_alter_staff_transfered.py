# Generated by Django 3.2.4 on 2021-10-31 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0037_auto_20211030_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='transfered',
            field=models.BooleanField(default=False, verbose_name='Transfered or not'),
        ),
    ]
