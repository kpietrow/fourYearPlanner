"""PreqRequisites"""
from django.db import models
from banner.models import Course


class Prerequisite(models.Model):
    """Prerequisite"""
    course = models.ForeignKey(Course)
    requirement = models.ForeignKey(Course)


class Meta:
    "Needed for separating models into files"
    app_label = "banner"
