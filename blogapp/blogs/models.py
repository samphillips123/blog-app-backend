from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=300)
    body = models.CharField(max_length=6000)