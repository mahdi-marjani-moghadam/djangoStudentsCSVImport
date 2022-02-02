from django.contrib import admin

from .models import parents

@admin.register(parents)
class parentsAdmin(admin.ModelAdmin):
    list_display = ("name", "age")

    # def show_parent(self, obj):
        
    #     result = parents.objects.filter(id=obj)
    #     return result["grade__avg"]
