from django.db import models
from django.contrib.auth.models import User


difficulty_choices = (
    (1, "Очень лёгкий"),
    (2, "Лёгкий"),
    (3, "Средний"),
    (4, "Сложный"),
    (5, "Очень сложный"),
)


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.IntegerField(choices=difficulty_choices)
    created_by = models.ForeignKey(User, models.PROTECT)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["difficulty"]
