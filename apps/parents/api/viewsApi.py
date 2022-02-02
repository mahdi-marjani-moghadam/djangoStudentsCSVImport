from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView

from .serializers import ParentSerializer
from ..models import parents





class ParentsList(ListCreateAPIView):
    queryset = parents.objects.all()
    serializer_class = ParentSerializer
    # permission_classes = [IsAuthenticated]




class ParentsRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = parents.objects.all()
    serializer_class = ParentSerializer
    # permission_classes = [IsAuthenticated]
