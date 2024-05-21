from django.db import models


# Create your models here.
class Admin(models.Model):
    login = models.CharField(max_length=60, blank=False)
    password = models.CharField(max_length=60, blank=False)

    def __str__(self):
        return self.login


class User(models.Model):
    login = models.CharField(max_length=60, blank=False)
    password = models.CharField(max_length=60, blank=False)

    def __str__(self):
        return self.login
