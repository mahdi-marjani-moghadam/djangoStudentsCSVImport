from django.urls import path
from . import views

urlpatterns = [
    path('', views.listView, name="student-list"),
    path('<pk>', views.detailView, name="student-detail"),
    
    path("upload/", views.StudentBulkUploadView.as_view(), name="student-upload"),

]
