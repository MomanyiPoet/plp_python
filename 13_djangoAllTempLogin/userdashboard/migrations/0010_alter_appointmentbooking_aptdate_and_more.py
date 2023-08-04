# Generated by Django 4.2.3 on 2023-08-04 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdashboard', '0009_rename_appointmentbook_appointmentbooking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentbooking',
            name='aptDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='appointmentbooking',
            name='aptNumber',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='appointmentbooking',
            name='serviceDescription',
            field=models.CharField(choices=[('Maintenance and Tune-ups', 'Maintenance and Tune-ups'), ('Brake and Suspension', 'Brake and Suspension'), ('Diagnostic Services', 'Diagnostic Services'), ('Not Sure, Select Other', 'Not Sure, Select Other')], default='Not Sure, Select Other', max_length=100),
        ),
    ]
