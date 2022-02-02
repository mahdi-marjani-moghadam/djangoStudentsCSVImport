from rest_framework import serializers

from ..models import parents

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = parents
        fields = ['id','name','age']

