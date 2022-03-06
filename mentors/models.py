from django.db import models

# Create your models here.
class Mentor(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200, blank=True)
    interests = models.CharField(max_length=200, default="None")
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.name