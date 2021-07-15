from .serializers import SongSerializer
from api_app.models import Songs
from rest_framework import generics


class SongAPIView(generics.ListAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer
