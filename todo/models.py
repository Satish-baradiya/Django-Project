from django.db import models
from django.db.models.base import Model

# Create your models here.


class NewTodo(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=200)


    def __str__(self):
        return f"Title : {self.title} | Description : {self.description}"

