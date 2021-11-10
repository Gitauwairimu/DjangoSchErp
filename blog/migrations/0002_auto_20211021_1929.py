# Generated by Django 3.2.4 on 2021-10-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='female', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(choices=[('Playgroup', 'Playgroup'), ('PP1', 'PP1'), ('PP2', 'PP2'), ('G1', 'G1'), ('G2', 'G2'), ('G3', 'G2'), ('G4', 'G2'), ('G5', 'G2'), ('G6', 'G2')], max_length=100),
        ),
    ]
