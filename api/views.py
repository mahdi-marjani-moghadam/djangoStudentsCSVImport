from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .serializers import StudentSerializer,PostSerializer,ParentSerializer
from home.models import parents, students,post
from rest_framework.generics import ListAPIView,ListCreateAPIView


class PostList(ListCreateAPIView):
    queryset = post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class ParentsList(ListCreateAPIView):
    queryset = parents.objects.all()
    serializer_class = ParentSerializer
    permission_classes = [IsAuthenticated]



class StudentsList(ListCreateAPIView):
    queryset = students.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]


