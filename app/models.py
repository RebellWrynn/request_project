from django.db import models

# Create your models here.

class employees(models.Model):
    id = models.ForeignKey(primary_key=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

class requests(models.Model):
    REQUEST_TYPE = {
        "S": "Обслуживание",
        "I": "Установка оборудования",
        "O": "Другой  вариант",
    }
    id = models.ForeignKey(primary_key=True)
    them = models.Charfield(max_length=30)
    requesttype = models.Charfield(max_length=30,choices = REQUEST_TYPE)
    priority = models.Charfield(max_length=30)
    description = models.Charfield(max_length=255)
    date = models.DateField()
    responsibleemployee = models.Charfield(max_length=30)
