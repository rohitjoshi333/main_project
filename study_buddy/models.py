from django.db import models

class Interest(models.Model):
    name = models.CharField(max_length=50, unique=True, default="no interest")  # unique optional

    def __str__(self):
        return self.name

class Student(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    interests = models.ManyToManyField(Interest)

    def __str__(self):
        return self.username
