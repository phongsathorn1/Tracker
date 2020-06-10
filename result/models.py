from django.db import models

# Create your models here.
class Sheet(models.Model):
    title = models.TextField(null=True, blank=True)
    description_info = models.TextField(null=True, blank=True)
    keywords_info = models.TextField(null=True, blank=True)