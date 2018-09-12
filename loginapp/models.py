from django.db import models

# Create your models here.
class UsersList(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
