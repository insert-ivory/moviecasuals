from django.db import models

from moviecasuals.accounts.models import MovieUserModel


class Director(models.Model):
    first_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )

    date_of_birth = models.DateField(
        blank=False,
        null=False,
    )

    biography = models.TextField()

    picture_url = models.URLField(
        blank=True,
        null=True,
    )

    user = models.ForeignKey(
        to=MovieUserModel,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    approved = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"