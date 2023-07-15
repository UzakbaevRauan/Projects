from django.db import models

# Create your models here.
class Job_title(models.Model):
    name = models.CharField(max_length=255)

class Employee(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    avatarUrl = models.URLField()
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    userTag = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    birthday = models.DateField()
    phone = models.CharField(max_length=15)