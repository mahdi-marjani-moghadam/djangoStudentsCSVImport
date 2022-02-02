from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import StudentSerializer
from ..models import students


class StudentsList(ListCreateAPIView):
    queryset = students.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [IsAuthenticated]


class StudentsRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = students.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [IsAuthenticated]
