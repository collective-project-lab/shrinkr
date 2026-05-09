from rest_framework import serializers
from .models import ShortenedURL


class ShortenedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ['short_code', 'long_url', 'created_at', 'click_count']
        read_only_fields = ['short_code', 'created_at', 'click_count']


class ShortenURLInputSerializer(serializers.Serializer):
    long_url = serializers.URLField()