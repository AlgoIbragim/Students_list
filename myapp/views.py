from django.shortcuts import render, get_object_or_404, redirect
from .models import Students
from .forms import StudentForm

def student_list(request):
    students = Students.objects.all()
    return render(request, 'students_list.html', {
        'students': students
    })

def student_info(request, pk):
    student = get_object_or_404(Students, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_info.html', {'form': form})

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_students.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Students, pk=pk)
    student.delete()
    return redirect('student_list')

