"""Minor Reqs"""
from django.db import models
from banner.models import Minor, Course


class Minor_Requirement(models.Model):
    """Minor Reqs"""
    minor = models.ForeignKey(Minor)
    course = models.ForeignKey(Course)


class Meta:
    "Needed for separating models into files"
    app_label = "banner"
