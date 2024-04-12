from django.db import models

class JsonData(models.Model):
    intensity = models.CharField(max_length=100)
    likelihood = models.CharField(max_length=100)
    relevance = models.CharField(max_length=100)
    year = models.CharField(max_length=255, default='Unknown')  # Set a default value
    country = models.CharField(max_length=100)
    topics = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.intensity} - {self.year} - {self.country}"
