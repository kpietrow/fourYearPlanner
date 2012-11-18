"""user section tracking for notifications"""
from django.db import models


class User_Sectin_Track(models.Model):
    """User tracking"""
    name = models.CharField(max_length=30)


class Meta:
    "Needed for separating models into files"
    app_label = "banner"
