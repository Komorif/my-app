from rest_framework import serializers
from .models import ModelVideo

class AnimeVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ModelVideo
        fields = '__all__'