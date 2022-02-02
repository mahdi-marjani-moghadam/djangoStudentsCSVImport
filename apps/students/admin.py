from django.contrib import admin
from .models import students
from apps.parents.models import parents

@admin.register(students)
class studentsAdmin(admin.ModelAdmin):
    list_display = ("name", "family","parent")

    # def show_parent(self, obj):
        
    #     result = parents.objects.filter(id=obj)
    #     return result["grade__avg"]


    
