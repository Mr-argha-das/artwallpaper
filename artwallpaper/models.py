from django.db import models

class User(models.Model):
    an_login_id = models.CharField(max_length=255)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=100)
    password = models.CharField(max_length=100)