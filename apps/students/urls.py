from django.urls import path
from . import views

urlpatterns = [
    path('', views.studentList.as_view(), name="students-list"),
    path('<int:pk>/', views.studentDetailViewExternalApi.as_view(),
         name="students-detail"),
    path('create/', views.create, name="students-create"),
    path("upload/", views.studentBulkUploadView.as_view(), name="students-upload"),
]
