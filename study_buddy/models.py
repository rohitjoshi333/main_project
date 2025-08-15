from django.db import models

class Interest(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    interests = models.ManyToManyField(Interest)

    def __str__(self):
        return self.username
