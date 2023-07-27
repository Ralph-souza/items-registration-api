from django.db import models


class LoanerGenderChoices(models.TextChoices):
    MALE = "male", "Male"
    FEMALE = "female", "Female"
