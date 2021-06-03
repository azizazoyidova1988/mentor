from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from mentor.models import *
from .forms import *
from . import services


def login_required_decorator(f):
    return login_required(f, login_url="login")


@login_required_decorator
def dashboard_page(request):
    courses = services.get_courses_count()
    trainers_count = services.get_trainers_count()
    events_count = services.get_events_count()
    students_count = services.get_students_count()
    subjects = services.get_subjects_all()[0]['count']
    front = services.get_frontend()[0]['count']
    backend = services.get_backend()[0]['count']
    status = {
        "all":subjects,
        "frontend": front,
        "backend": backend
    }

    ctx = {
        "courses": courses,
        "trainers_count": trainers_count,
        "events_count": events_count,
        "students_count": students_count,
        "status": status,
        "subjects": subjects

    }
    return render(request, 'dashboard/index.html', ctx)


def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')


def dashboard_logout(request):
    logout(request)
    return redirect('login')


def courses_list(request):
    courses = services.get_courses()
    ctx = {
        "courses": courses
    }
    return render(request, 'dashboard/courses/list.html', ctx)


def courses_create(request):
    model = Courses()
    form = CourseForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('courses_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/courses/form.html', ctx)


def courses_edit(request, course_id):
    model = Courses.objects.get(id=course_id)
    form = CourseForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('courses_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/courses/form.html', ctx)


def courses_delete(request, course_id):
    model = Courses.objects.get(id=course_id)
    model.delete()
    return redirect("courses_list")


def trainers_list(request):
    trainers = services.get_trainers()
    ctx = {
        "trainers": trainers
    }
    return render(request, 'dashboard/trainer/list.html', ctx)


def trainers_create(request):
    model = Trainer()
    form = TrainerForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('trainers_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/trainer/form.html', ctx)


def trainers_edit(request, trainer_id):
    model = Trainer.objects.get(id=trainer_id)
    form = TrainerForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('trainers_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/trainer/form.html', ctx)


def trainers_delete(request, trainer_id):
    model = Trainer.objects.get(id=trainer_id)
    model.delete()
    return redirect("trainers_list")


def students_list(request):
    students = services.get_students()
    ctx = {
        "students": students
    }
    return render(request, 'dashboard/student/list.html', ctx)


def students_create(request):
    model = Students()
    form = StudentForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('students_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/student/form.html', ctx)


def students_edit(request, student_id):
    model = Students.objects.get(id=student_id)
    form = StudentForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('students_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/student/form.html', ctx)


def students_delete(request, student_id):
    model = Students.objects.get(id=student_id)
    model.delete()
    return redirect("students_list")


def events_list(request):
    events = services.get_events()
    ctx = {
        "events": events
    }
    return render(request, 'dashboard/events/list.html', ctx)


def events_create(request):
    model = Events()
    form = EventForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('events_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/events/form.html', ctx)


def events_edit(request, event_id):
    model = Events.objects.get(id=event_id)
    form = EventForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('events_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/events/form.html', ctx)


def events_delete(request, event_id):
    model = Events.objects.get(id=event_id)
    model.delete()
    return redirect("events_list")


# def subject_count_list(request):
#     status = services.get_subjects_all()
#     filter = "all"
#     if request.GET:
#         filter = request.GET.get("order_filter")
#
#         if filter == "frontend":
#             status = services.get_frontend()
#
#         if filter == "backend":
#             status = services.get_backend()
#
#     ctx = {
#         "status": status,
#         "filter": filter,
#     }
#     return render(request, 'dashboard/student/list.html', ctx)
#
#
# def status(request, pk, status):
#     model = Students.objects.get(id=pk)
#     model.status = status
#     model.save()
#     return redirect("subject_list")
