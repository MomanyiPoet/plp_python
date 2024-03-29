# Generated by Django 4.2.3 on 2023-07-27 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aboutDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pageName', models.CharField(max_length=20)),
                ('pageDescription', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'tblabout',
            },
        ),
        migrations.CreateModel(
            name='contactDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagename', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('timing', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tblcontactdetails',
            },
        ),
    ]
