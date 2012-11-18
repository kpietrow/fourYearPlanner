"""Professor"""
from django.db import models
from django.contrib.auth.models import User


class Professor(models.Model):
    """Professor"""
    user = models.OneToOneField(User)


class Meta:
    "Needed for separating models into files"
    app_label = "banner"
