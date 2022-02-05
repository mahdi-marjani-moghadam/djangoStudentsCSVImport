from email.policy import default
from rest_framework import serializers

from ..models import students
from apps.parents.models import parents


class StudentSerializer(serializers.ModelSerializer):
    parent = parents.objects.all()
    url = serializers.HyperlinkedIdentityField(
        view_name='student_detail', read_only=True)

    class Meta:
        model = students
        fields = ['id', 'name', 'family',  'parent', 'url']
