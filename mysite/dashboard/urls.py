from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_page, name="dashboard"),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('trainer/list/', views.trainers_list, name="trainers_list"),
    path('trainer/add/', views.trainers_create, name="trainers_add"),
    path('trainer/<int:trainer_id>/edit/', views.trainers_edit, name="trainers_edit"),
    path('trainer/<int:trainer_id>/delete/', views.trainers_delete, name="trainers_delete"),

    path('courses/list/', views.courses_list, name="courses_list"),
    path('courses/add/', views.courses_create, name="courses_add"),
    path('courses/<int:course_id>/edit/', views.courses_edit, name="courses_edit"),
    path('courses/<int:course_id>/delete/', views.courses_delete,name="courses_delete"),

    path('events/list/', views.events_list, name="events_list"),
    path('events/add/', views.events_create, name="events_add"),
    path('events/<int:event_id>/edit/', views.events_edit, name="events_edit"),
    path('events/<int:event_id>/delete/', views.events_delete, name="events_delete"),

    path('student/list/', views.students_list, name="students_list"),
    path('student/add/', views.students_create, name="students_add"),
    path('student/<int:student_id>/edit/', views.students_edit, name="students_edit"),
    path('student/<int:student_id>/delete/', views.students_delete, name="students_delete"),

    # path("status/<int:pk>/<int:status>", views.status, name="status"),

    # path('status/list/', views.subject_count_list, name='subject_list'),
]