# Generated by Django 4.2.3 on 2023-10-14 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_App', '0007_alter_patient_bmi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='BMI',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='DiabetesPedigreeFunction',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=10),
        ),
    ]
