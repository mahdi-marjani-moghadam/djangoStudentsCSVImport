from django.urls import path,re_path
from . import viewsApi

urlpatterns = [

    path('', viewsApi.ParentsList.as_view(), name='parent-list'),
    re_path(r'^(?P<pk>\d+)/$', viewsApi.ParentsRetrieveUpdateDestroy.as_view(), name='parents-detail'),

]
