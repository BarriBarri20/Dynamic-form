from django.contrib import admin
from django.db import models
from .models import Session, Course


class SessionInLineAdmin(admin.TabularInline):
    model = Session


class CourseAdmin(admin.ModelAdmin):
    inlines = [SessionInLineAdmin]


admin.site.register(Course)