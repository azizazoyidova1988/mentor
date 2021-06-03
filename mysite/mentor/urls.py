from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('courses/', views.courses, name="courses"),
    path('courses/<int:courses_id>/course-details/', views.course_details, name="course_details"),
    path('events/', views.events, name="events"),
    path('trainers/', views.trainers, name="trainers"),
    path('contact/', views.contact, name="contact"),
    path('email/', views.contact_email, name="email"),
    path('dashboard/',include('dashboard.urls'))
]
