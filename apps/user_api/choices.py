from django.db import models


class UserGenderChoices(models.TextChoices):
    MALE = "male", "Male"
    FEMALE = "female", "Female"
