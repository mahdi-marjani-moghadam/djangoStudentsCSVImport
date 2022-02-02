from django.contrib import admin
from django.urls import path,re_path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', include('apps.home.urls')),

    path('students/', include('apps.students.urls')),
    # path('parents/', include('apps.parents.urls')),

    path('api/v1/',include('apps.core.urls')),
    path('/api-auth/', include('rest_framework.urls')),

]
