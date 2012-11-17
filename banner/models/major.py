"""Major"""
from django.db import models


class Major(models.Model):
    """Major"""
    name = models.CharField(max_length=30)


class Meta:
    "Needed for separating models into files"
    app_label = "banner"
