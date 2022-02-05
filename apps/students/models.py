from django.db import models

from apps.core.models import baseModel
from apps.parents.models import parents


class students(baseModel):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    parent = models.ForeignKey(parents, on_delete=models.CASCADE)
    
    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, default="male")
    

    STATUS_CHOICES = [("active", "Active"), ("inactive", "Inactive")]
    current_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active"
    )

    def __str__(self):
        return f"{self.name} {self.family} {self.parent}"


class StudentBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to="students/bulkupload/")
    
    def __str__(self):
        return f"{self.csv_file} "

