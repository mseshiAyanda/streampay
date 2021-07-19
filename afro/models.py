from django.db import models
import psycopg2 as Database

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Content(models.Model):
    name = models.CharField(max_length=40)
    type_of_content=models.CharField(max_length=40)
    description=models.CharField(max_length=200)
    links=models.CharField(max_length=40)
    Video_content=models.FileField(upload_to="video/%y",blank=True)