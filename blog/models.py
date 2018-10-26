from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    CONDITION = (
        ('Rescatado', 'Rescatado'),
        ('Disponible', 'Disponible'),
        ('Adoptado', 'Adoptado'),
    )

    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField()
    condition = models.TextField(choices=CONDITION, default='Rescatado')
    picture = models.ImageField(
        upload_to='user_pics', default='default.jpg')

    def __str__(self):
        return self.name
