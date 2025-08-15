from django.contrib import admin
from .models import Student, Interest

admin.site.register(Student)
admin.site.register(Interest)


# student_matching/urls.py
from django.urls import path
from .views import student_match_view, student_register_view

urlpatterns = [
    path('match/<int:student_id>/', student_match_view, name='student_match'),
    path('register/', student_register_view, name='student_register'),
]