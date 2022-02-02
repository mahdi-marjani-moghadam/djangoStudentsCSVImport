from django.urls import path, include

from . import viewsApi

urlpatterns = [
    path('', viewsApi.StudentsList.as_view(), name='student_list'),
]
