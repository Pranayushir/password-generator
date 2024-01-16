from django.db import models


class GeneratedPassword(models.Model):
    password = models.CharField(max_length=100)

# Create your models here.
