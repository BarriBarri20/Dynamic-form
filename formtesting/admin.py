from django.contrib import admin
from .models import Session, Course, Assignment, Skill

from django.contrib import admin
from .models import Course, Session, Assignment


class AssignmentInline(admin.TabularInline):
    model = Assignment
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name", )


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "course")
    list_display_links = ("name", )

    inlines = (AssignmentInline, )
