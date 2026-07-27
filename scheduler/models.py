from django.db import models


class DummyUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class DateRecord(models.Model):

    TIME_CHOICES = (
        ("PST", "PST"),
        ("UTC", "UTC"),
    )

    datetime_value = models.DateTimeField()

    timezone = models.CharField(
        max_length=3,
        choices=TIME_CHOICES,
        default="PST"
    )

    def __str__(self):
        return f"{self.datetime_value} ({self.timezone})"


class ConversionState(models.Model):
    DIRECTION_CHOICES = (
        ("PST_TO_UTC", "PST_TO_UTC"),
        ("UTC_TO_PST", "UTC_TO_PST"),
    )

    direction = models.CharField(
        max_length=20,
        choices=DIRECTION_CHOICES,
        default="PST_TO_UTC",
    )

    batch = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.direction} - Batch {self.batch}"