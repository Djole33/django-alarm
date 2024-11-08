from django.db import models
from django.utils import timezone
from datetime import timedelta

class Timer(models.Model):
    name = models.CharField(max_length=30)
    duration = models.DurationField()
    start_time = models.DateTimeField(blank=True, default=timezone.now)

    def __str__(self):
        return self.name

    def get_end_time(self):
        """Calculate the time when the timer will go off."""
        return self.start_time + self.duration

    def remaining_time(self):
        """Calculate how much time is left until the timer goes off."""
        time_left = self.get_end_time() - timezone.now()
        return max(time_left, timedelta(seconds=0))

    def is_time_up(self):
        """Check if the timer has reached its end time."""
        return timezone.now() >= self.get_end_time()