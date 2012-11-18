"""Times"""
from django.db import models
from banner.models import Section


class Section_Time(models.Model):
    """Times"""
    section = models.ForeignKey(Section)
    day_of_week = models.SmallIntegerField() # 0 = Sunday, 1= Monday....
    start_time = models.TimeField()
    end_time = models.TimeField()


class Meta:
    "Needed for separating models into files"
    app_label = "banner"
