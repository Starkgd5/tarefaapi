from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    STATUS_CHOICES = [
        (PENDING, 'Pendente'),
        (IN_PROGRESS, 'Em Andamento'),
        (COMPLETED, 'Concluído')
    ]

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
