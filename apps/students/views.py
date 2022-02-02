import csv
import requests

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.views.generic import ListView
# from django.http import HttpResponse

# from urllib import response
# from urllib.request import Request
# from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
# from django.views.decorators.csrf import csrf_exempt

from .models import students, StudentBulkUpload
from apps.parents.models import parents

# class StudentsList(View):
#     @csrf_exempt
#     def dispatch(self, request, *args, **kwargs):
#         if(request.method == 'GET'):
#             return self.listView(request)
#         else:
#             return JsonResponse(
#                 status=405,
#                 data={
#                     'status':'error', 'message':'Method Not Allowed'
#                 }
#             )

# def listView(self,request):
#     response = requests.get('http://127.0.0.1:8000/api/v1/students/')
#     StudentsResponse = response.json()

#     data = {
#         "students": StudentsResponse
#     }
#     return data


# def listView(request):
#     response = requests.get('http://127.0.0.1:8000/api/v1/students/')
#     StudentsResponse = response.json()

#     data = {
#         "students": StudentsResponse
#     }

#     return render(request, 'front/list.html', data)


def detailView(request, *args, **kwargs):

    response = requests.get(
        'http://127.0.0.1:8000/api/v1/students/'+kwargs['pk'])
    StudentResponse = response.json()

    data = {
        "student": StudentResponse
    }

    return render(request, 'front/detail.html', data)


class StudentList(ListView):
    model = students
    data = ""
    template_name = 'front/list.html'
    context_object_name = ""

    def get_context_data(self, **kwargs):
        context = super(StudentList, self).get_context_data(**kwargs)

        response = requests.get('http://127.0.0.1:8000/api/v1/students/')
        StudentsResponse = response.json()

        data = {
            "students": StudentsResponse
        }
        context['data'] = data

        return context


class StudentBulkUploadView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = StudentBulkUpload
    template_name = "admin/students_upload.html"
    fields = ["csv_file"]
    success_url = "/admin/students/students"
    success_message = "Successfully uploaded students"
    # form_class = SteudenstForm

    # def post(self, request, *args, **kwargs):
    #     user = students(name='ali',family='karimi',parent=parents.objects.get(id=1))
    #     print('------------------------')
    #     print(user)
    #     print('------------------------')
    #     print(request)
    #     print('------------------------')
    #     return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        new_group = form.save()
        with new_group.csv_file.open('rt') as the_csv:

            fieldnames = ['name', 'family', 'gender',
                          'parent_name', 'parent_age']
            data_file = csv.DictReader(
                the_csv, fieldnames=fieldnames, delimiter=',', dialect=csv.excel)

            for row in data_file:

                if(row['name'] == 'name'):
                    continue

                parent = parents(
                    name=row['parent_name'],
                    age=int(row['parent_age'])
                )
                parent.save()

                student = students(
                    name=row['name'],
                    family=row['family'],
                    gender=row['gender'],
                    parent=parents.objects.get(id=parent.id)
                )
                student.save()
        return super(StudentBulkUploadView, self).form_valid(form)
