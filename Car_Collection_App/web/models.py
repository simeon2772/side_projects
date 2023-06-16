from enum import Enum

from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def check_if_year_valid(value):
    if not (1980 < value < 2049):
        raise ValidationError("Year must be between 1980 and 2049")


class CarChoices(Enum):
    SPORT_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    @classmethod
    def choices(cls):
        return ((choice.name, choice.value) for choice in cls)


class Profile(models.Model):
    MAX_LEN_USERNAME = 10
    MIN_LEN_USERNAME = 2
    MAX_LEN_PASSWORD = 30
    MAX_LEN_FIRST_NAME = 30
    MAX_LEN_LAST_NAME = 30

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        validators=[
            validators.MinLengthValidator
            (MIN_LEN_USERNAME, "The username must be a minimum of 2 chars")],
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_LEN_PASSWORD,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        null=False,
        blank=False,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Car(models.Model):
    class Meta:
        ordering = ['pk']

    MAX_LEN_TYPE = 10
    MAX_LEN_MODEL = 20
    MIN_LEN_MODEL = 2
    MIN_LEN_PRICE = 1

    type = models.CharField(
        max_length=MAX_LEN_TYPE,
        null=False,
        blank=False,
        choices=CarChoices.choices()
    )

    model = models.CharField(
        max_length=MAX_LEN_MODEL,
        validators=[
            validators.MinLengthValidator(MIN_LEN_MODEL)
        ],
        null=False,
        blank=False,
    )

    year = models.PositiveIntegerField(
        validators=[check_if_year_valid],
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )
