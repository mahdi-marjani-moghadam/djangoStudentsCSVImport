from django.urls import path
from . import views

urlpatterns = [
    path('', views.studentList.as_view(), name="student-list"),
    path('<int:pk>/', views.StudentDetailViewExternalApi.as_view(), name="student-detail"),
    
    path("upload/", views.StudentBulkUploadView.as_view(), name="student-upload"),
]
