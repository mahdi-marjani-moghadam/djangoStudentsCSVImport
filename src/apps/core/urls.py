from django.urls import path, include

urlpatterns = [
    path('students/', include('apps.students.api.urls')),
    path('parents/', include('apps.parents.api.urls')),
]