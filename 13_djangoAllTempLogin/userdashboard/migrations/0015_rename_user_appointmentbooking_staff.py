# Generated by Django 4.2.3 on 2023-08-04 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdashboard', '0014_alter_appointmentbooking_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointmentbooking',
            old_name='user',
            new_name='staff',
        ),
    ]
