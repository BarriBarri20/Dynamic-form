from django import forms
from django.forms.models import inlineformset_factory
from django.contrib.admin import widgets as widget_element
from django.contrib.admin import site as admin_site
from tinymce import TinyMCE

from .models import Assignment, Course, Session, Skill, LearningOutcome


class TinyMCEWidget(TinyMCE):

    def use_required_attribute(self, *args):
        return False


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SessionForm(forms.ModelForm):

    class Meta:
        model = Session

        fields = [
            'name',
            'session_description',
        ]
        widgets = {
            'name':
            forms.TextInput(attrs={'class': 'form-control'}),
            'session_description':
            TinyMCEWidget(attrs={
                'required': False,
                'cols': 30,
                'rows': 10
            }),
        }


class LearningOutcomeForm(forms.ModelForm):

    class Meta:
        model = LearningOutcome
        fields = ['learningoutcome', 'skills']
        widgets = {
            'learningoutcome': forms.TextInput(attrs={
                'class': 'form-control rich-text',
                'id': 'richtext_field'
            }),
            'skills': forms.SelectMultiple(attrs={
                'class': 'border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            }),
        }

    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        required=False,
        blank=True,
    )


class AssignmentForm(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = ['title', 'description', 'est_time', 'submission_delay']
        widgets = {
            'title':
            forms.TextInput(
                attrs={
                    'class':
                    'block w-full p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
                }),
            'description':
            forms.Textarea(
                attrs={
                    'class':
                    'block w-full p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
                }),
            'est_time':
            forms.NumberInput(
                attrs={
                    'class':
                    'block w-full p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
                }),
            'submission_delay':
            forms.NumberInput(
                attrs={
                    'class':
                    'block w-full p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
                }),
        }


class SkillForm(forms.ModelForm):

    class Meta:

        model = Skill

        fields = ['skillname']
