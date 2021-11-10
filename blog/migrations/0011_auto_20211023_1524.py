# Generated by Django 3.2.4 on 2021-10-23 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20211023_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='grade',
            field=models.CharField(choices=[('Playgroup', 'Playgroup'), ('PP1', 'PP1'), ('PP2', 'PP2'), ('G1', 'G1'), ('G2', 'G2'), ('G3', 'G3'), ('G4', 'G4'), ('G5', 'G5'), ('G6', 'G6'), ('General_teacher', 'General Teacher'), ('support_staff', 'Support Staff'), ('admin_staff', 'Administrative Staff')], max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(choices=[('Playgroup', 'Playgroup'), ('PP1', 'PP1'), ('PP2', 'PP2'), ('G1', 'G1'), ('G2', 'G2'), ('G3', 'G3'), ('G4', 'G4'), ('G5', 'G5'), ('G6', 'G6'), ('General_teacher', 'General Teacher'), ('support_staff', 'Support Staff'), ('admin_staff', 'Administrative Staff')], max_length=100),
        ),
    ]
