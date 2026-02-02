from django.db import models


class Session(models.Model):
    DAY_CHOICES = [
        (i, d)
        for i, d in enumerate(
            ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], start=1
        )
    ]
    day = models.IntegerField(choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=160, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["day", "start_time"]

    def __str__(self):
        return f"{self.name} ({self.get_day_display()} {self.start_time})"
