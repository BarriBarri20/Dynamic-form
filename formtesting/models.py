# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from tinymce import models as tinymce_models


class Course(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("course_detail", kwargs={"pk": self.pk})


class Skill(models.Model):
    skillname = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'Skill'

    def __str__(self):
        return self.skillname


class Session(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    session_description = tinymce_models.HTMLField(
        help_text="Session Description", blank=True, null=True)
    #    learningoutcome = models.CharField(help_text="Learning outcome",
    #                                        max_length=256,
    #                                        blank=True,
    #                                        null=True)
    skill = models.ManyToManyField(Skill)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = 'Session'


class Assignment(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    est_time = models.FloatField(validators=[MinValueValidator(0.00)],
                                 null=True,
                                 blank=True)
    submission_delay = models.FloatField(validators=[MinValueValidator(0.00)],
                                         null=True,
                                         blank=True)
    session = models.ForeignKey(Session,
                                on_delete=models.CASCADE,
                       
                                blank=True,
                                null=True)

    class Meta:
        db_table = 'Assignment'
