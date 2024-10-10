# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Employees(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'employees'


class Requests(models.Model):
    them = models.CharField(max_length=30)
    requesttype = models.CharField(max_length=30)
    priority = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    date = models.DateField()
    responsibleemployee = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'requests'
