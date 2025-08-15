from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from .utils import match_students

def student_register_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student_match', student_id=student.id)
    else:
        form = StudentForm()
    return render(request, 'student_matching/register.html', {'form': form})

def student_match_view(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    matched_students = match_students(student_id)
    return render(request, 'student_matching/match_results.html', {
        'student': student,
        'matched_students': matched_students
    })
