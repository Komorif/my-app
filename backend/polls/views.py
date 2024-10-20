from django.http import HttpResponse
from rest_framework.views import APIView

from .models import ModelVideo
from .serializer import AnimeVideoSerializer
from rest_framework.response import Response


# Для БД


class AnimeVideoView(APIView):
    def get(self, request):
        output = [
            {
                "title": output.title,
                "description": output.description
            } for output in ModelVideo.objects.all()
        ]
        return Response(output)
    
    def post(self, request):
        serializer = AnimeVideoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)