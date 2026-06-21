"""Legacy models kept for historical migrations; replaced by letting and profiles apps."""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator
from django.contrib.auth.models import User


class Address(models.Model):
    """Legacy address model (superseded by letting.Address)."""

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        """Return the street number and name."""
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """Legacy letting model (superseded by letting.Letting)."""

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name="old_letting")

    def __str__(self):
        """Return the letting title."""
        return self.title


class Profile(models.Model):
    """Legacy profile model (superseded by profiles.Profile)."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="old_profile")
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Return the associated username."""
        return self.user.username
