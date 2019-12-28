from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_id = models.CharField(max_length=20)
    password = models.CharField(max_length=16)
    ph_number = models.BigIntegerField()
    address = models.CharField(max_length=300, default='')
    email = models.EmailField(max_length=30)
    gender = models.CharField(max_length=6)
