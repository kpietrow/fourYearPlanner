"""Phone"""
from django.db import models
from django.contrib.auth.models import User
from django_localflavor_us.models import PhoneNumberField


class Phone(models.Model):
    """Phone"""
    user = models.OneToOneField(User)
    phone = PhoneNumberField()


class Meta:
    "Needed for separating models into files"
    app_label = "banner"
