from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    """Course"""
    name = models.CharField(max_length=30)
    is_restricted = models.BooleanField()


class Major(models.Model):
    """Major"""
    name = models.CharField(max_length=30)


class Major_Requirement(models.Model):
    """Major Reqs"""
    major = models.ForeignKey(Major)
    course = models.ForeignKey(Course)


class Minor(models.Model):
    """Minor"""
    name = models.CharField(max_length=30)


class Minor_Requirement(models.Model):
    """Minor Reqs"""
    minor = models.ForeignKey(Minor)
    course = models.ForeignKey(Course)


class Phone(models.Model):
    """Phone"""
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=10)


class Prerequisite(models.Model):
    """Prerequisite"""
    course = models.ForeignKey(Course,related_name= 'course')
    requirement = models.ForeignKey(Course,related_name='requirement')


class Professor(models.Model):
    """Professor"""
    user = models.OneToOneField(User)


class Semester(models.Model):
    """Semester"""
    name = models.CharField(max_length=50)


class Section(models.Model):
    """Section"""
    max_size = models.PositiveSmallIntegerField()
    course = models.ForeignKey(Course)
    semester = models.ForeignKey(Semester)
    professor = models.ForeignKey(Professor)


class Section_Time(models.Model):
    """Times"""
    section = models.ForeignKey(Section)
    day_of_week = models.SmallIntegerField() # 0 = Sunday, 1= Monday....
    start_time = models.TimeField()
    end_time = models.TimeField()



class User_Section_Track(models.Model):
    """User tracking"""
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=20)

