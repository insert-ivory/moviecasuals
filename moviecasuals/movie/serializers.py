from rest_framework import serializers

from moviecasuals.movie.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    director_full_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'director_full_name', 'description', 'genre_choices']


    def get_director_full_name(self, obj):
        return obj.director.get_full_name()