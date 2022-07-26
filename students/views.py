from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from students.models import Student


def index(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students/index.html', context)


def add(request):
    return render(request, 'students/add.html')


def insert(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    age = request.POST.get('age')
    student = Student(first_name=first_name, last_name=last_name, age=age)
    student.save()
    return HttpResponseRedirect('/students/')


def edit(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {'student': student}
    return render(request, 'students/edit.html', context)


def update(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.first_name = request.POST.get('first_name')
    student.last_name = request.POST.get('last_name')
    student.age = request.POST.get('age')
    student.save()
    return HttpResponseRedirect('/students/')


def delete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return HttpResponseRedirect('/students/')
