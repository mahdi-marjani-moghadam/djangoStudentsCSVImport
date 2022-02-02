from django.urls import path
from . import views

urlpatterns = [
    path('posts', views.PostList.as_view(), name='post_list'),
    path('parents', views.ParentsList.as_view(), name='student_list'),
    path('students', views.StudentsList.as_view(), name='student_list'),

]
