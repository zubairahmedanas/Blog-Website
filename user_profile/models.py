from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


# Create your models here.


class User(AbstractUser):
    email = models.EmailField(
        max_length=150,
        unique=True,
        error_messages={"unique": "the email must be unique"},
    )
    profile_image = models.ImageField(
        null=True,
        blank=True,
        upload_to="profile_images"
    )
    REQUIRED_FIELDS = ["email"]
    objects = CustomUserManager()

    def __str__(self):
        return self.username
