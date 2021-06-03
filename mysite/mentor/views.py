from django.shortcuts import render, redirect
from .services import *
from .models import *
from .forms import *


def home(request):
    abouts = get_abouts()
    resources = get_resources()
    courses = get_courses()
    trainers = get_trainers()

    ctx = {
        "abouts": abouts,
        "resources": resources,
        "courses": courses,
        "trainers": trainers,
        'home_page':'active'

    }

    return render(request, 'mentor/index.html', ctx)


def about(request):
    abouts = get_abouts()
    writers = get_comment_writers()
    ctx = {
        "abouts": abouts,
        "writers": writers,
        'about_page': 'active'

    }

    return render(request, 'mentor/about.html', ctx)


def courses(request):
    courses = get_courses()
    # cour=Courses.objects.all().filter(courses_id=courses_id)
    ctx = {
        "courses": courses,
        'course_page': 'active'

    }
    return render(request, 'mentor/courses.html', ctx)


def course_details(request, courses_id):
    courses = get_courses()
    # print(courses)
    courses_details = get_courses_details(courses_id)
    print(courses_details)
    ctx = {
        "courses_details": courses_details,
        "courses": courses,

    }
    return render(request, 'mentor/course-details.html', ctx)


def events(request):
    events = get_events()
    ctx = {
        "events": events,
        'event_page': 'active'
    }
    return render(request, 'mentor/events.html', ctx)


def trainers(request):
    trainers = get_trainers()
    ctx = {

        "trainers": trainers,
        'trainer_page': 'active'
    }
    return render(request, 'mentor/trainers.html', ctx)



def contact(request):
    modal = Students()
    form = StudentForm(request.POST or None, instance=modal)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    ctx={
        'contact_page': 'active'
    }

    return render(request, 'mentor/contact.html',ctx)


def contact_email(request):
    email = Students()
    if request.POST:
        email.email = request.POST.get("email")
        email.save()
    return render(request, 'mentor/index.html')
