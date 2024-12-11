from django.test import TestCase
from django.db import IntegrityError

from moviecasuals.movie.models import Movie, Rating
from moviecasuals.director.models import Director
from moviecasuals.accounts.models import MovieUserModel
from moviecasuals.movie_choices import MovieChoices


class MovieModelTest(TestCase):
    def setUp(self):

        self.movie_user = MovieUserModel.objects.create_user(
            username="john_doe", email="john@example.com", password="password"
        )

        self.director = Director.objects.create(
            first_name="Steven",
            last_name="Spielberg",
            date_of_birth="1946-12-18",
            biography="Biography text goes here.",
            user=self.movie_user
        )

        self.movie = Movie.objects.create(
            user=self.movie_user,
            director=self.director,
            picture_url="https://example.com/movie.jpg",
            description="A great movie about something.",
            title="Jurassic Park",
            genre_choices="Action",
            approved=True
        )

    def test_create_valid_movie(self):
        movie = self.movie
        self.assertEqual(movie.title, "Jurassic Park")
        self.assertEqual(movie.genre_choices, "Action")
        self.assertTrue(movie.approved)
        self.assertEqual(movie.director, self.director)

    def test_unique_title(self):
        with self.assertRaises(IntegrityError):
            Movie.objects.create(
                user=self.movie_user,
                director=self.director,
                picture_url="https://example.com/movie2.jpg",
                description="Another movie.",
                title="Jurassic Park",
                genre_choices="Adventure",
            )

    def test_default_values(self):
        movie = Movie.objects.create(
            user=self.movie_user,
            director=self.director,
            picture_url="https://example.com/movie3.jpg",
            description="Movie with default values.",
            title="Test Movie",
        )
        self.assertFalse(movie.approved)
        self.assertEqual(movie.genre_choices, MovieChoices.OTHERS)

    def test_average_rating(self):
        movie = self.movie

        self.movie_user2 = MovieUserModel.objects.create_user(
            username="another_user", email="another@example.com", password="password"
        )
        Rating.objects.create(
            movie=movie,
            user=self.movie_user,
            rating=5
        )
        Rating.objects.create(
            movie=movie,
            user=self.movie_user2,
            rating=3
        )
        self.assertEqual(movie.average_rating(), 4)
