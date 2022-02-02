from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView

from .serializers import StudentSerializer
from ..models import  students


# class PostList(ListCreateAPIView):
#     queryset = post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)



class StudentsList(ListCreateAPIView):
    queryset = students.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [IsAuthenticated]


