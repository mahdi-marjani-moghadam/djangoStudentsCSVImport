from re import template
import requests
from django.shortcuts import render
from django.views.generic.list import ListView

from apps.students.models import students



def homeView(request):
    response = requests.get('https://reqres.in/api/users?page=2')
    UserResponse = response.json()

    data = {
        "students": students.objects.all().order_by('-id'),
        "users": UserResponse['data']
    }
    
    return render(request,'front/home.html',data)
