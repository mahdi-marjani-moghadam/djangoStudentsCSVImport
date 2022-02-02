# import imp
# from timeit import default_timer
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"