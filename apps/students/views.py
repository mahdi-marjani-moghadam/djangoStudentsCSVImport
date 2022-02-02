from urllib import response
from urllib.request import Request
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import students

class Students(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if(request.method == 'GET'):
            return self.listView(request)
        else:
            return JsonResponse(
                status=405,
                data={
                    'status':'error', 'message':'Method Not Allowed'
                }
            )
    
    def listView(self,request):
        return students.objects.all()