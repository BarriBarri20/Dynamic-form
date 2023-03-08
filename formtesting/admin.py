from django.contrib import admin
from .models import Session, Course, Assignment, Skill, LearningOutcome
from django.db import models
from django_summernote.admin import SummernoteModelAdmin


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
class SessionAdmin(SummernoteModelAdmin):
    summernote_fields = ('session_description', )
    list_display = ("id", "name", "course")
    list_display_links = ("name", )

    inlines = (AssignmentInline, LearningOutcomeInline)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("skillname", )
