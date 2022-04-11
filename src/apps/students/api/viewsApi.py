from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import StudentSerializer
from ..models import students


class StudentsList(ListCreateAPIView):
    queryset = students.objects.all().order_by('-id')
    serializer_class = StudentSerializer
    # permission_classes = [IsAuthenticated]


class StudentsRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = students.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [IsAuthenticated]

class StudentReport(ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return students.objects.filter(parent__age__gte=self.kwargs['age'])
        
        
    
