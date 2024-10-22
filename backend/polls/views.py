from django.http import HttpResponse
from rest_framework.views import APIView

from .models import ModelVideo
from .serializer import AnimeVideoSerializer
from rest_framework.response import Response




class AnimeVideoView(APIView):
    def get(self, request):
        output = [
            {
                "image": request.build_absolute_uri(video.image.url) if video.image else None,
                "title": video.title,
                "genre": video.genre,
                "date": video.date,
                "month": video.month,
                "description": video.description
            } for video in ModelVideo.objects.all()
        ]
        return Response(output)
    
    def post(self, request):
        serializer = AnimeVideoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)