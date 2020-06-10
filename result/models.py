from django.db import models

# Create your models here.


class Sheet(models.Model):
    title = models.TextField()
    url = models.URLField()
    description_info = models.TextField()
    keywords_indo = models.TextField()

    def __str__(self):
        return self.title
