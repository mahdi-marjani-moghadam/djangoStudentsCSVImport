from django.shortcuts import render
import requests
from apps.students.models import students

def homeView(request):


    response = requests.get('https://reqres.in/api/users?page=2')
    UserResponse = response.json()

    data = {
        "posts": students.objects.all().order_by('-id'),
        "users": UserResponse['data']
    }
    
    return render(request,'front/home.html',data)