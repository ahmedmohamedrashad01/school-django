from django.shortcuts import render, redirect
from .forms import AddEmployee, EditEmployee
from . models import Student
from django.contrib import messages
# Create your views here.


def home(request):

    if request.method == 'POST':
        employee = AddEmployee(request.POST)
        if employee.is_valid():
            name = employee.cleaned_data.get('name')
            address = employee.cleaned_data.get('address')
            age = employee.cleaned_data.get('age')
            studentclass = employee.cleaned_data.get('studentclass')
            std = Student(name=name, address=address,
                          age=age, studentclass=studentclass)
            std.save()
            messages.success(request, 'Student has been added')
            return render(request, 'pages/index.html', {'emp': AddEmployee})
    else:
        return render(request, 'pages/index.html', {'emp': AddEmployee})


def display(request):
    data = Student.objects.all()
    return render(request, 'pages/display.html', {'data': data})


def delete(request, std_id):
    std = Student.objects.get(pk=std_id)
    std.delete()
    return redirect('display')


def edit(request, std_id):
    std = Student.objects.get(pk=std_id)
    if request.method == 'POST':
        form = EditEmployee(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            address = form.cleaned_data.get('address')
            age = form.cleaned_data.get('age')
            studentclass = form.cleaned_data.get('studentclass')
            std = Student(pk=std_id, name=name, address=address,
                          age=age, studentclass=studentclass)
            std.save()
            return redirect('display')
    else:

        std = Student.objects.get(pk=std_id)
        form = EditEmployee(initial={'name': std.name, 'address': std.address,
                            'age': std.age, 'studentclass': std.studentclass})
        return render(request, 'pages/edit.html', {'form': form})
