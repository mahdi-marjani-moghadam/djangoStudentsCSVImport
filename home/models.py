from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('title','content')


    def __str__(self):
        return f"{self.title}"

class parents(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
   

    def __str__(self):
        return f"{self.name} {self.age}"

class students(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    parent = models.ForeignKey(parents, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('name','family')

    def __str__(self):
        return f"{self.name} {self.family} {self.parent}"

