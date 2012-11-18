"""Phone"""
from django.db import models
from django.contrib.auth.models import User


class Phone(models.Model):
    """Phone"""
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=10)


class Meta:
    "Needed for separating models into files"
    app_label = "banner"
