from django.urls import path, include ,re_path


from . import viewsApi

urlpatterns = [
    path('', viewsApi.StudentsList.as_view(), name='students-list'),
    re_path(r'^(?P<pk>\d+)/$', viewsApi.StudentsRetrieveUpdateDestroy.as_view(), name='students-detail'),

    path('report/<age>', viewsApi.StudentReport.as_view(), name='students-report'),
]
