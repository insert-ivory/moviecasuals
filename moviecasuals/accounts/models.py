from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from moviecasuals.accounts.managers import MovieUserManager


class MovieUserModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=20,
        unique=True
    )

    email = models.EmailField(
        unique=True,
        blank=False,
        null=False
    )

    first_name = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    last_name = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = MovieUserManager()

    def __str__(self):
        return self.username
