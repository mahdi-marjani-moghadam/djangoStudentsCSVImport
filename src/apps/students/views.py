import csv
from django.shortcuts import render
import requests

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView


from .models import students, StudentBulkUpload
from apps.parents.models import parents
from .forms import createStudent


class studentList(ListView):
    model = students
    paginate_by = 3
    template_name = 'front/list.html'


class studentDetailViewExternalApi(DetailView):

    model = students
    template_name = 'front/detail.html'

    def get_context_data(self, **kwargs):

        # two ways get data
        # 1
        return {
            'student': students.get_by_pk(self.kwargs['pk']),
        }

        # 2
        response = requests.get(
            'http://127.0.0.1:8000/api/v1/students/'+str(self.kwargs['pk']))
        StudentResponse = response.json()

        return {
            'student': StudentResponse
        }


class studentBulkUploadView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = StudentBulkUpload
    template_name = "admin/students_upload.html"
    fields = ["csv_file"]
    success_url = "/admin/students/students"
    success_message = "Successfully uploaded students"
    # form_class = SteudenstForm

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
        return super(studentBulkUploadView, self).form_valid(form)


def create(request):
    if(request.method == 'POST'):
        form = createStudent(request.POST)
        if form.is_valid():
            student = form.save()
    else:
        form = createStudent()

    return render(request, 'front/create.html', {'form': form})
