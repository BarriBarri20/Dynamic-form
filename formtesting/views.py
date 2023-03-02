from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from .forms import AssignmentForm, CourseForm, SessionForm, SkillForm
from .models import Course, Session, Assignment, Skill


def create_session(request, pk):
    course = Course.objects.get(id=pk)
    # sessions = Session.objects.filter(course=course)
    form = SessionForm(request.POST or None)
    form.fields['skill'].required = False
    if request.method == 'POST':
        if form.is_valid():

            session = form.save(commit=False)
            session.course = course
            session.save()
            return redirect('detail-session', pk=session.pk)

        else:
            return render(request, 'partials/session_form.html',
                          {'form': form})

    context = {'form': form, 'course': course}

    return render(request, 'create_session.html', context)


def update_session(request, pk):
    session = Session.objects.get(id=pk)
    form = SessionForm(request.POST or None, instance=session)
    form.fields['skill'].required = False
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('session-detail', pk=session.id)
    context = {'form': form, 'session': session}

    return render(request, 'partials/session_form.html', context)

    return render(request, 'formtesting/book_form.html', {'form': form})


def delete_session(request, pk):
    session = get_object_or_404(Session, id=pk)

    if request.method == 'POST':
        session.delete()
        return HttpResponse('Session deleted')

    return HttpResponseNotAllowed(['POST'])


def detail_session(request, pk):
    session = get_object_or_404(Session, id=pk)
    assignments = Assignment.objects.filter(session=session)
    context = {'session': session, 'assignments': assignments}

    return render(request, 'partials/session_detail.html', context)


def create_session_form(request):
    form = SessionForm()
    context = {'form': form}
    form.fields['skill'].required = False

    return render(request, 'partials/session_form.html', context)


"""   Assigment views """


def create_assignment(request, pk):
    session = Assignment.objects.get(id=pk)
    # assignments = Assignment.objects.filter(session=session)
    form = AssignmentForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.course = session

            return redirect('detail-assignment', pk=assignment.pk)

        else:
            return render(request, 'partials/assignment_form.html',
                          {'form': form})

    context = {'form': form, 'session': session}

    return render(request, 'create_assignment.html', context)


def update_assignment(request, pk):
    assignment = Assignment.objects.get(id=pk)
    form = AssignmentForm(request.POST or None, instance=assignment)

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect('assignment-detail', pk=assignment.id)
    context = {'form': form, 'assignment': assignment}

    return render(request, 'partials/assignment_form.html', context)

    return render(request, 'formtesting/book_form.html', {'form': form})


def delete_assignment(request, pk):
    assignment = get_object_or_404(Assignment, id=pk)

    if request.method == 'POST':
        assignment.delete()
        return HttpResponse('Assignment deleted')

    return HttpResponseNotAllowed(['POST'])


def detail_assignment(request, pk):
    assignment = get_object_or_404(Assignment, id=pk)
    assignments = Assignment.objects.filter(assignment=assignment)
    context = {'assignment': assignment, 'assignments': assignments}

    return render(request, 'partials/assignment_detail.html', context)


def create_assignment_form(request):
    form = AssignmentForm(request.POST or None)
    context = {'form': form}
    return render(request, 'partials/assignment_form.html', context)


""" Skill views """


def create_skill(request, pk):
    assignment = Assignment.objects.get(id=pk)
    skills = Skill.objects.filter(assignment=assignment)
    form = SkillForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            skill = form.save(commit=False)
            skill.assignment = assignment
            skill.save()
            return redirect('skill-detail', pk=skill.pk)

        else:
            return render(request, 'partials/skill_form.html', {'form': form})

    context = {'form': form, 'assignment': assignment, 'skills': skills}

    return render(request, 'create_skill.html', context)


def update_skill(request, pk):
    skill = Skill.objects.get(id=pk)
    form = SkillForm(request.POST or None, instance=skill)

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect('skill-detail', pk=skill.id)
    context = {'form': form, 'skill': skill}

    return render(request, 'partials/skill_form.html', context)

    return render(request, 'formtesting/book_form.html', {'form': form})


def delete_skill(request, pk):
    skill = get_object_or_404(Skill, id=pk)

    if request.method == 'POST':
        skill.delete()
        return HttpResponse('Skill deleted')

    return HttpResponseNotAllowed(['POST'])


def detail_skill(request, pk):
    skill = get_object_or_404(Skill, id=pk)
    assignments = Assignment.objects.filter(skill=skill)
    context = {'skill': skill, 'assignments': assignments}

    return render(request, 'partials/skill_detail.html', context)


def create_skill_form(request):
    form = SkillForm(request.POST or None)
    context = {'form': form}
    return render(request, 'partials/skill_form.html', context)
