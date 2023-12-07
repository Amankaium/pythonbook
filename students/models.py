from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    phone_number = models.CharField(max_length=30)
    programming_language = models.CharField(
        max_length=20,
        choices=(
            ('py', 'Python'),
            ('js', 'JavaScript'),
            ('java', 'java'),
            ('c#', 'C#')
        )
    )