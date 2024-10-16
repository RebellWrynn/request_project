# Generated by Django 5.0.7 on 2024-10-08 03:21

from django.db import migrations

def create_data(apps,shema_editor):
    employees = apps.get_model('app','employees')
    employees(firstname='ivan',lastname='ivanovish',surname='ivanov')
    employees(firstname='roman',lastname='romanovish',surname='romanov')



class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data)
    ]

