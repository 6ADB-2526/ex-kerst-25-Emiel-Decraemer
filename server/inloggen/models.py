from django.db import models

# Create your models here.

class gebruikers(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    role = models.CharField(max_length=10)
    isSuperuser = models.BooleanField(default=False)