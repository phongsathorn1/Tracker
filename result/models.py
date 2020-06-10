from django.db import models

# Create your models here.
class Sheet(models.Model):
    Title = models.TextField(null=True, blank=True)
    Body = models.TextField(null=True, blank=True)
    Score = models.IntegerField(null=True, blank=True)