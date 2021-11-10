# Generated by Django 3.2.4 on 2021-10-31 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0042_alter_announcement_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('details', models.TextField()),
            ],
        ),
    ]
