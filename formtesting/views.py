from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import AssignmentForm, CourseForm, SessionForm, LearningOutcomeForm
from .models import Course, Session, Assignment, LearningOutcome
from django.forms import formset_factory

SessionFormSet = formset_factory(SessionForm, extra=0)


def create_course(request, pk=None):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            return redirect('detail-course', pk=course.pk)
    else:
        course = Course.objects.create()
        course_id = course.id
        form = CourseForm()

    return render(request, 'create_course.html', {
        'form': form,
        'course_id': course_id,
    })


def create_session(request, pk=None, ck=None):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            session = form.save()
            return redirect('detail-session', pk=session.pk)

    course = get_object_or_404(Course, id=ck)
    session = Session.objects.create(course=course)
    session.save()
    session_id = session.id
    form = SessionForm()

    context = {'form': form, 'sk': session_id}
    return render(request,
                  template_name='partials/session_form.html',
                  context=context)


def create_assignment(request, pk=None, sk=None):

    assignment = Assignment.objects.create(session=Session.objects.get(id=sk))
    assignment.save()
    assignment_id = assignment.id
    form = AssignmentForm()
    return render(request, 'partials/assignment_form.html', {
        'form': form,
        'assignment_id': assignment_id
    })


def create_learningoutcome(request, pk=None, sk=None):

    learningoutcome = LearningOutcome.objects.create(
        session=Session.objects.get(id=sk))
    learningoutcome.save()
    learningoutcome_id = learningoutcome.id
    form = LearningOutcomeForm()
    return render(request, 'partials/learningoutcome_form.html', {
        'form': form,
        'learningoutcome_id': learningoutcome_id
    })



def edit_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course_form = CourseForm(instance=course)
    sessions_and_forms = []
    for session in Session.objects.filter(course=course):
        session_form = SessionForm(instance=session)
        sessions_and_forms.append((session.id, session_form))
    context = {
        'course': course,
        'sessions_and_forms': sessions_and_forms,
        'course_id': course_id,
        'course_form': course_form,
    }
    return render(request, 'edit_course.html', context)


def edit_learningoutcome(request, sk):
    session = Session.objects.get(id=sk)
    assignments_and_forms = []
    for assignment in Assignment.objects.filter(session=session):
        assignment_form = AssignmentForm(instance=assignment)
        assignments_and_forms.append((assignment.id, assignment_form))
        
    learningoutcomes_and_forms = []
    
    for learningoutcome in LearningOutcome.objects.filter(session=session):
        learningoutcome_form = LearningOutcomeForm(instance=learningoutcome)
        learningoutcomes_and_forms.append((learningoutcome.id, learningoutcome_form))
    context = {
        'session': session,
        'learningoutcomes_and_forms': learningoutcomes_and_forms,
    }
    return render(request, 'partials/update_learningoutcome_form.html', context)


def edit_assignment(request, sk):
    print('called!')
    session = Session.objects.get(id=sk)
    assignments_and_forms = []
    for assignment in Assignment.objects.filter(session=session):
        assignment_form = AssignmentForm(instance=assignment)
        assignments_and_forms.append((assignment.id, assignment_form))
        
    learningoutcomes_and_forms = []
    
    for learningoutcome in LearningOutcome.objects.filter(session=session):
        learningoutcome_form = LearningOutcomeForm(instance=learningoutcome)
        learningoutcomes_and_forms.append((learningoutcome.id, learningoutcome_form))
    context = {
        'session': session,
        'assignments_and_forms': assignments_and_forms,
        'learningoutcomes_and_forms': learningoutcomes_and_forms,
    }
    return render(request, 'partials/update_assignment_form.html', context)


def edit_session(request, pk):
    if request.method == 'POST':
        print(request.POST)
        form = SessionForm(request.POST, instance=Session.objects.get(id=pk))
        if form.is_valid():
            form.save()

        return HttpResponse('Session updated')

    session = get_object_or_404(Session, id=pk)
    form = SessionForm(instance=session)
    

    context = {
        'session-form': form,
        'sk': session.id,
        'assignments': Assignment.objects.filter(session=session),
        'learningoutcomes': LearningOutcome.objects.filter(session=session)
    }
    return render(request, 'edit_session.html', context)


def update_course(request, pk):
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=Course.objects.get(id=pk))
        if form.is_valid():
            form.save()

        return HttpResponse('Course updated')


def update_session(request, pk):
    if request.method == 'POST':
        print(request.POST)
        form = SessionForm(request.POST, instance=Session.objects.get(id=pk))
        if form.is_valid():
            form.save()

        return HttpResponse('Session updated')


def update_assignment(request, pk):
    if request.method == 'POST':
        form = AssignmentForm(request.POST,
                              instance=Assignment.objects.get(id=pk))
        if form.is_valid():
            form.save()

        return HttpResponse('Assignment updated')


def update_learningoutcome(request, pk):
    if request.method == 'POST':

        learningoutcome = get_object_or_404(LearningOutcome, pk=pk)

        form = LearningOutcomeForm(request.POST, instance=learningoutcome)
        print(form.errors)
        if form.is_valid():
            print("okay")
            form.save()

        return HttpResponse('Learning Outcome updated')


def delete_session(response, pk):
    session = get_object_or_404(Session, id=pk)
    session.delete()
    return HttpResponse('Session deleted')


def delete_assignment(response, pk):
    print(pk)
    assignment = get_object_or_404(Assignment, id=pk)
    assignment.delete()
    return HttpResponse('Assignment deleted')


def delete_learningoutcome(response, pk):
    print("done hereeee")
    learningoutcome = get_object_or_404(LearningOutcome, id=pk)
    learningoutcome.delete()
    return HttpResponse('Learning Outcome deleted')