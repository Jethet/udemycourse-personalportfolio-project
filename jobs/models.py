from django.db import models

# generally speaking, you will have one model per app
# Django documentation has info on model field types to choose from

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=250)
