from django.urls import path
from . import viewsApi

urlpatterns = [

    path('', viewsApi.ParentsList.as_view(), name='student_list'),
]
