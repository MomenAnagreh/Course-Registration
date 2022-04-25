from django.db import models
from django.contrib.auth.models import User

# python manage.py makemigrations
# python manage.py migrate

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    student = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title