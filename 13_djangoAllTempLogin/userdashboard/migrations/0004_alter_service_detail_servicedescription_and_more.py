# Generated by Django 4.2.3 on 2023-08-02 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdashboard', '0003_alter_service_detail_creationdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_detail',
            name='servicedescription',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='service_detail',
            name='servicename',
            field=models.CharField(max_length=50),
        ),
    ]
