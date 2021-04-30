from rest_framework import serializers
from core.models import Movie

class MovieDetailsSerializer(serializers.ModelSerializer):
    """
    Movie serializer
    """
    class Meta:
        model = Movie
        fields = (
            "id",
            "name",
            "duration",
            "description",
            "rating",
            "release_date",
        )
