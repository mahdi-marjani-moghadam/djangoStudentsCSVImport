from urllib import response
from urllib.request import Request
from django.shortcuts import render


import requests

from . import models
# from . import serializers

# class ListPost(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         posts = models.post.objects.all()
#         serializer = serializers.PostSerializer(posts,many=True)
#         return Response(serializer) 


def homeView(request):


    data = requests.get('https://reqres.in/api/users?page=2')
    data = data.json()

    data = {
        "posts": models.post.objects.all().order_by('-id'),
        "users": data['data']
    }
    return render(request,'front/home.html',data)