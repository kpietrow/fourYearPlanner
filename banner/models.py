from django.db import models
from django.contrib.auth.models import User


class Major(models.Model):
    """Major"""
    name = models.CharField(max_length=30)
    user = models.ManyToManyField(User)

    def __unicode__(self):
        return unicode(self.pk)


class Course(models.Model):
    """Course"""
    name = models.CharField(max_length=30)
    is_restricted = models.BooleanField()
    major = models.ForeignKey(Major)

    def __unicode__(self):
        return unicode(self.pk)


class Major_Requirement(models.Model):
    """Major Reqs"""
    major = models.ForeignKey(Major)
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return unicode(self.pk)


class Minor(models.Model):
    """Minor"""
    name = models.CharField(max_length=30)
    user = models.ManyToManyField(User)

    def __unicode__(self):
        return unicode(self.pk)


class Minor_Requirement(models.Model):
    """Minor Reqs"""
    minor = models.ForeignKey(Minor)
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return unicode(self.pk)


class Phone(models.Model):
    """Phone"""
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=10)

    def __unicode__(self):
        return unicode(self.pk)


class Prerequisite(models.Model):
    """Prerequisite"""
    course = models.ForeignKey(Course,related_name= 'course')
    requirement = models.ForeignKey(Course,related_name='requirement')

    def __unicode__(self):
        return unicode(self.pk)


class Professor(models.Model):
    """Professor"""
    user = models.OneToOneField(User)

    def __unicode__(self):
        return unicode(self.pk)


class Semester(models.Model):
    """Semester"""
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.pk)


class Section(models.Model):
    """Section"""
    max_size = models.PositiveSmallIntegerField()
    course = models.ForeignKey(Course)
    semester = models.ForeignKey(Semester)
    professor = models.ForeignKey(Professor)
    user = models.ManyToManyField(User)

    def __unicode__(self):
        return unicode(self.pk)


class Section_Time(models.Model):
    """Times"""
    section = models.ForeignKey(Section)
    day_of_week = models.SmallIntegerField() # 0 = Sunday, 1= Monday....
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __unicode__(self):
        return unicode(self.pk)


class User_Section_Track(models.Model):
    """User tracking"""
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=20)

    def __unicode__(self):
        return unicode(self.pk)


def can_register(self, section):
    # TODO optimize
    sections = self.section_set.all()
    majors = self.major_set.all()
    conditions = []
    conditions.append(section not in sections)
    for prereq in section.course.course.all():
        conditions.append(prereq.requirement in [x.course for x in sections])
    if section.course.is_restricted:
        conditions.append(section.course.major in majors)
    if False in conditions:
        return False
    return True

User.add_to_class('can_register', can_register)
