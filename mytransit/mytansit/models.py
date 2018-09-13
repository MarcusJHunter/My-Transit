from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, null=True, blank=True)
    interest = models.TextField(null=True, blank=True)
    picture= models.ImageField(upload_to='user/%Y/%m/%d/', null=True, blank=True)
    updated = models.BooleanField(default=False)
    def __str__(self):
        return self.name


