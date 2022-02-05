from django.urls import reverse
from django.db import models

from apps.core.models import baseModel

class parents(baseModel):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return "{}".format(self.name)

