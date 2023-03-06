from django.contrib import admin
from .models import Session, Course, Assignment, Skill, LearningOutcome
from django.db import models
from tinymce.widgets import TinyMCE


class AssignmentInline(admin.TabularInline):
    model = Assignment
    extra = 1


class LearningOutcomeInline(admin.TabularInline):
    model = LearningOutcome
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name", )


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "course")
    list_display_links = ("name", )
    formfield_overrides = {models.TextField: {'widget': TinyMCE()}}

    inlines = (AssignmentInline, LearningOutcomeInline)
