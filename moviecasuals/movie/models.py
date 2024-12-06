from django.core.validators import MaxLengthValidator
from django.db import models
from django.db.models import Avg

from moviecasuals.accounts.models import MovieUserModel
from moviecasuals.director.models import Director
from moviecasuals.movie_choices import MovieChoices


class Movie(models.Model):
    user = models.ForeignKey(
        to=MovieUserModel,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    director = models.ForeignKey(
        to=Director,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    picture_url = models.URLField(
        blank=False,
        null=False,
    )

    description = models.TextField(
        validators=[MaxLengthValidator(2000)],
        help_text="Description should not exceed 2000 characters."
    )

    title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )
    approved = models.BooleanField(
        default=False
    )

    genre_choices = models.CharField(
        max_length=50,
        choices=MovieChoices.choices,
        default=MovieChoices.OTHERS,
    )

    def __str__(self):
        return self.title

    def average_rating(self):
        return self.ratings.aggregate(Avg('rating'))['rating__avg'] or 0


class Comment(models.Model):
    movie = models.ForeignKey(
        to=Movie,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    user = models.ForeignKey(
        to=MovieUserModel,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {str(self.movie)}"


class Rating(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='ratings'
    )

    user = models.ForeignKey(
        to=MovieUserModel,
        on_delete=models.CASCADE
    )

    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    class Meta:
        unique_together = ('movie', 'user')


