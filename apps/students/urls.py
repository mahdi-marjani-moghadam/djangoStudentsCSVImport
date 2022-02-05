from django.urls import path
from . import views

urlpatterns = [
    path('', views.studentList.as_view(), name="student-list"),
    path('<int:pk>/', views.studentDetailViewExternalApi.as_view(), name="students-detail"),
    
    path("upload/", views.studentBulkUploadView.as_view(), name="student-upload"),
]
