from django import forms
from django.forms.models import inlineformset_factory

from .models import Assignment, Course, Session, Skill


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['name']


class SessionForm(forms.ModelForm):

    class Meta:
        model = Session
        fields = '__all__'
        fields = ['name', 'session_description', 'learningoutcome', 'skill']
        widgets = {
            'name':
            forms.TextInput(attrs={'class': 'form-control'}),
            'session_description':
            forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'richtext_field'
            }),
            'learnigoutcome':
            forms.NumberInput(attrs={'class': 'form-control'}),
            'skill':
            forms.NumberInput(attrs={'class': 'form-control'}),
        }


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


SessionFormSet = inlineformset_factory(Course,
                                       Session,
                                       form=SessionForm,
                                       min_num=1,
                                       extra=1,
                                       can_delete=True)

AssignmentFormSet = inlineformset_factory(Session,
                                          Assignment,
                                          form=AssignmentForm,
                                          min_num=1,
                                          extra=1,
                                          can_delete=True)
