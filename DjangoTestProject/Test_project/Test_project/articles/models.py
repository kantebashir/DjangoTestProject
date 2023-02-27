from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Test_project(models.Model):
    title = models.CharField(_MAX_LENGTH=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    #add in thumbnail later
    #add in author later
