# Generated by Django 4.2.3 on 2023-10-14 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_App', '0006_alter_patient_bmi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='BMI',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='patient',
            name='DiabetesPedigreeFunction',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
