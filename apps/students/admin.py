import requests
from django.contrib import admin
from django.db.models import Count

from .models import students
from apps.parents.models import parents


@admin.register(students)
class studentsAdmin(admin.ModelAdmin):
    list_display = ("name", "family", "parent", "parent_age")

    @admin.display()
    def parent_age(self, obj):
        return obj.parent.age

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['greate60'] = parents.objects.filter(
            age__gte=60).aggregate(all=Count("id"))

        response = requests.get(
            'http://127.0.0.1:8000/api/v1/students/report/50')
        extra_context['greate50'] = len(response.json())

        return super(studentsAdmin, self).changelist_view(request, extra_context=extra_context)
