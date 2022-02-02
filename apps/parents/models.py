from django.db import models

class parents(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
