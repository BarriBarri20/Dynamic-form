from django import forms
from django.forms.models import inlineformset_factory
from django.contrib.admin import widgets as widget_element
from django.contrib.admin import site as admin_site

from .models import Assignment, Course, Session, Skill


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['name']


class SessionForm(forms.ModelForm):

    class Meta:
        model = Session

        fields = [
            'name',
            'session_description',
            'skill',
        ]
        widgets = {
            'name':
            forms.TextInput(attrs={'class': 'form-control'}),
            'session_description':
            forms.Textarea(attrs={
                'class': 'form-control rich-text',
                'id': 'richtext_field'
            }),
        }
        skill = forms.ModelMultipleChoiceField(
            Skill.objects.all(),
            widget=widget_element.RelatedFieldWidgetWrapper(
                widget=widget_element.FilteredSelectMultiple(
                    'Keywords', False),
                rel=Session.skill.rel,
                admin_site=admin_site),
            required=False,
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

        skillname = forms.ModelChoiceField(
            queryset=Skill.objects.all(),
            to_field_name='skillname',
            required=False,
            widget=forms.Select(attrs={'class': 'form-control'}))


# SessionFormSet = inlineformset_factory(Course,
#                                        Session,
#                                        form=SessionForm,
#                                        min_num=1,
#                                        extra=1,
#                                        can_delete=True)

# AssignmentFormSet = inlineformset_factory(Session,
#                                           Assignment,
#                                           form=AssignmentForm,
#                                           min_num=1,
#                                           extra=1,
#                                           can_delete=True)
