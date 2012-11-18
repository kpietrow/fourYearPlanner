"""Section"""
from django.db import models
from banner.models import Course, Semester, Professor


class Section(models.Model):
    """Section"""
    max_size = models.PositiveSmallIntegerField()
    course = models.ForeignKey(Course)
    semester = models.ForeignKey(Semester)
    professor = models.ForeignKey(Professor)


class Meta:
    "Needed for separating models into files"
    app_label = "banner"
