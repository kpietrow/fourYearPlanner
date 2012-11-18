from django.contrib import admin
from banner.models import Course, Major_Requirement, Minor_Requirement, Phone, Prerequisite, Professor, Semester, Section_Time, User_Section_Track, Major, Section

class CourseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Course, CourseAdmin)
class MajorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Major, MajorAdmin)

class Major_RequirementsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Major_Requirement, Major_RequirementsAdmin)

class Minor_RequirementAdmin(admin.ModelAdmin):
    pass

admin.site.register(Minor_Requirement, Minor_RequirementAdmin)

class PhoneAdmin(admin.ModelAdmin):
    pass
admin.site.register(Phone, PhoneAdmin)

class PrerequisiteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Prerequisite, PrerequisiteAdmin)

class ProfessorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Professor, ProfessorAdmin)

class SemesterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Semester, SemesterAdmin)

class SectionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Section, SectionAdmin)

class Section_TimeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Section_Time, Section_TimeAdmin)

class User_Section_TrackAdmin(admin.ModelAdmin):
    pass

admin.site.register(User_Section_Track, User_Section_TrackAdmin)
