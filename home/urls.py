from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name="home-page"),
    #     path(r'^$', views.ListPost.as_view(), name='post_list'),
]
