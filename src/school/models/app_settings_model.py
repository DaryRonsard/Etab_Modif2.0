from django.db import models

from base.models.helpers.date_time_model import DateTimeModel


class AppSettingsModel(DateTimeModel):
    smtp_server = models.CharField(max_length=150)
    smtp_port = models.IntegerField()
    smtp_username = models.CharField(max_length=150)
    smtp_password = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.smtp_server} - {self.smtp_username}"

    class Meta:
        verbose_name = "Paramètre appli"
        verbose_name_plural = "Paramètre applis"