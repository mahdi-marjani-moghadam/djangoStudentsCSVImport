from dataclasses import field
from rest_framework import serializers

from home.models import parents, students, post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        fields = ['id','title', 'content', 'time', 'owner','owner_id']
        model = post


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = parents
        fields = ['id','name','age']

class StudentSerializer(serializers.ModelSerializer):
    parent = parents.objects.all()

    class Meta:
        model = students
        fields = ['id', 'name', 'family', 'parent','parent_id']


