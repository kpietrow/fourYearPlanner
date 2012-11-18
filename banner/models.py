from django.db import models
from django.contrib.auth.models import User


class Major(models.Model):
    """Major"""
    name = models.CharField(max_length=30)
    user = models.ManyToManyField(User)




class Course(models.Model):
    """Course"""
    name = models.CharField(max_length=30)
    is_restricted = models.BooleanField()
    major = models.ForeignKey(Major)


class Major_Requirement(models.Model):
    """Major Reqs"""
    major = models.ForeignKey(Major)
    course = models.ForeignKey(Course)


class Minor(models.Model):
    """Minor"""
    name = models.CharField(max_length=30)
    user = models.ManyToManyField(User)


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
    user = models.ManyToManyField(User)


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


def can_register(self, section):
    # TODO optimize
    sections = self.section_set.all()
    majors = self.major_set.all()
    conditions = []
    conditions.append(section not in sections)
    for prereq in section.course.requirement.all():
        conditions.append(prereq.requirement in [x.course for x in sections])
    if section.course.is_restricted:
        conditions.append(section.course.major in majors)
    if False in conditions:
        return False
    return True

User.add_to_class('can_register', can_register)
