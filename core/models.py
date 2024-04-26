from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = [
    ('Pendente', 1),
    ('Em Andamento', 2),
    ('Concluido', 3)
]
# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
