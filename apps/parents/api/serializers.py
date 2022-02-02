from rest_framework import serializers

from ..models import parents

class ParentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='parent_detail', read_only=True)

    class Meta:
        model = parents
        fields = ['id','name','age','url']

