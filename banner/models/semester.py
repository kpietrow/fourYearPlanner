"""Semester"""
from django.db import models


class Semester(models.Model):
    """Semester"""
    name = models.CharField(max_length=30)


class Meta:
    "Needed for separating models into files"
    app_label = "banner"
