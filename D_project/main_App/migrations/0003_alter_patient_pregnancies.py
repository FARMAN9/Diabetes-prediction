# Generated by Django 4.2.3 on 2023-09-10 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_App', '0002_alter_patient_outcome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Pregnancies',
            field=models.IntegerField(default=0),
        ),
    ]
