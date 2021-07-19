from django.db import models


class SiteAvailability(models.Model):
    is_uptime = models.BooleanField()
    status = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        availability = "Uptime" if self.is_uptime else "Downtime"
        return f"{availability} - {self.status}"
