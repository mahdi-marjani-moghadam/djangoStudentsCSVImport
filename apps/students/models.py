from django.db import models
from apps.parents.models import parents

# from django.utils import timezone
# from django.contrib.auth.models import User


# class post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     time = models.DateTimeField(default=timezone.now)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)

#     class Meta:
#         ordering = ('title','content')


#     def __str__(self):
#         return f"{self.title}"


class students(models.Model):
    STATUS_CHOICES = [("active", "Active"), ("inactive", "Inactive")]

    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]


    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    parent = models.ForeignKey(parents, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")

    current_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active"
    )

    class Meta:
        ordering = ('name','family')

    def __str__(self):
        return f"{self.name} {self.family} {self.parent}"

