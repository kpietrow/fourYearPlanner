"""Minor"""
from django.db import models


class Minor(models.Model):
    """Minor"""
    name = models.CharField(max_length=30)


class Meta:
    "Needed for separating models into files"
    app_label = "banner"
