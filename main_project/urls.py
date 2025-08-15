# main_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('student_register')),  # redirect / to /register/
    path('', include('study_buddy.urls')),
]