from rest_framework import serializers
from user.models import TopAnime


class TopAnimeSerializer(serializers.ModelSerializer):
    """

    """

    def create(self, validated_data):
        instance = TopAnime.objects.create(**validated_data)
        return instance

    class Meta:
        model = TopAnime
        fields = ('name', 'total_seasons', 'total_likes')
