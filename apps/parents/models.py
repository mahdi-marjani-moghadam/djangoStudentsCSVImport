from django.db import models

class parents(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
   

    def __str__(self):
        return f"{self.name}"
