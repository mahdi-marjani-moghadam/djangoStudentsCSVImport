from django.db import models
from django.forms import CharField
from django.urls import reverse
from django.http import Http404

from apps.parents.models import parents

from django.utils import timezone

# from adaptor.model import CsvModel

class baseModel(models.Model):

    class Meta:
        abstract = True
    
    @classmethod
    def get_by_pk(cls, pk, raise_exception=False):
        obj = cls.objects.filter(pk=pk).first()
        if raise_exception and not obj:
            raise Http404('The requested entity is not found')
        return obj

class students(baseModel):
    STATUS_CHOICES = [("active", "Active"), ("inactive", "Inactive")]

    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]

    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    parent = models.ForeignKey(parents, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, default="male")
    created_at = models.DateTimeField(default=timezone.now)

    current_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active"
    )

    # team_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)


    class Meta:
        ordering = ('-id', 'family')

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name} {self.family} {self.parent}"


class StudentBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to="students/bulkupload/")
    
    def __str__(self):
        return f"{self.csv_file} "

# class MyCsvModel(CsvModel):
#     name = CharField()
#     family = CharField()
#     gender = CharField()
    
#     class Meta:
#         # dbModel = students
#         delimiter = ";"
