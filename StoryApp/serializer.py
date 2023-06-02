from rest_framework import serializers
from .models import Detail

class Detail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ['id', 'title', 'story']