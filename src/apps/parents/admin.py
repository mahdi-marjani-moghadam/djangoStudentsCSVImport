from django.contrib import admin

from .models import parents

@admin.register(parents)
class parentsAdmin(admin.ModelAdmin):
    list_display = ("name", "age")
    search_fields = ['name','age']
    list_filter = ['age']
    list_display_links = ['name']
