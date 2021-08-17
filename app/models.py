from django.db import models

# Create your models here.


class Person(models.Model):
    heading = models.CharField(max_length=255)
  