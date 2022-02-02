from django.shortcuts import render

# Create your views here.
def homeView(request):
    data = {
        "users" :[
            {
                'id':1
            },
            {
                'id':2
            }
        ]
    }
    return render(request,'front/home.html',data)