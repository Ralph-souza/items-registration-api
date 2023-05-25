from django.db import models


class GamesFormatChoices(models.TextChoices):
    PHYSICAL = "physical", "Physical"
    DIGITAL = "digital", "Digital"


class GamesPlatformChoices(models.TextChoices):
    PLAYSTATION_4 = "playstation 4", "Playstation 4"
    NINTENDO_SWITCH = "nintendo switch", "Nintendo Switch"


class VideoTypeChoices(models.TextChoices):
    MOVIES = "movies", "Movies"
    SERIES = "series", "Series"


class VideoFormatChoices(models.TextChoices):
    DVD = "dvd", "DVD"
    BLURAY = "blu_ray", "Blu-ray"
    DIGITAL = "digital", "Digital"


class PrintedTypeChoices(models.TextChoices):
    PHYSICAL = "physical", "Physical"
    DIGITAL = "digital", "Digital"


class PrintedFormatChoices(models.TextChoices):
    BOOK = "book", "Book"
    COMICS = "comics", "Comics"
    DIGITAL = "digital", "Digital"


class LoanesStatusChoices(models.TextChoices):
    LOANED = "loaned", "Loaned"
    NOT_LOANED = "not_loaned", "Not_loaned"
