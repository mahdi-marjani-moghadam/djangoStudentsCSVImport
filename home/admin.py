from django.contrib import admin
from .models import post,students,parents


@admin.register(students)
class studentsAdmin(admin.ModelAdmin):
    list_display = ("name", "family")

    def show_parent(self, obj):
        
        result = parents.objects.filter(id=obj)
        return result["grade__avg"]


@admin.register(post)
class postAdmin(admin.ModelAdmin):
    list_display = ("title", "content")

    
