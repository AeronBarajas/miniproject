from .models import Mini
from rest_framework import serializers

class MiniSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mini # The model to be serialized
        fields = ['id', 'title', 'body'] #the fields that are included in output