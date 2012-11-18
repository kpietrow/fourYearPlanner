"""Course"""
from django.db import models


class Course(models.Model):
    """Course"""
    name = models.CharField(max_length=30)
    is_restricted = models.BooleanField()


class Meta:
    "Needed for separating models into files"
    app_label = "banner"
