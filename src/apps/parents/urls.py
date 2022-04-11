from django.urls import path
from . import views

urlpatterns = [
    path('', views.parentList.as_view(), name="parent-list"),
    path('<int:pk>/', views.parentDetailView.as_view(), name="parents-detail"),
    
]
