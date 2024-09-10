from django.db import models

# Create your models here.

class employees(models.Model):
    firstname = models.CharField(max_leigth=30)
    lastname = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

class requests(models.Model):
    REQUEST_TYPE = {
        "S": "Обслуживание",
        "I": "Установка оборудования",
        "O": "Другой  вариант",
        

    }
    them = models.Charfield(max_leigth=30)
    requesttype = models.Charfield(max_leigth=30,choices = REQUEST_TYPE)
    priority = models.Charfield(max_leigth=30)
    description = models.Charfield(max_leigth=255)
    date = models.DateField()
    responsibleemployee = models.Charfield(max_leigth=30)
