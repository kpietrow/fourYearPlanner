"""Major Req"""
from django.db import models
from banner.models import Major, Course


class Major_Requirement(models.Model):
    """Major Reqs"""
    major = models.ForeignKey(Major)
    course = models.ForeignKey(Course)

class Meta:
    "Needed for separating models into files"
    app_label = "banner"
