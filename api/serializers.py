from rest_framework import serializers
from api_app.models import Songs


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ('artist', 'album', 'title', 'year')
