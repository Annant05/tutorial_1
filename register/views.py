import json

from django.http import HttpResponse
from django.shortcuts import render

from register.models import Student


def index(request):
    return render(request, 'register/register.html')


student_list = []


def registered(request):
    student = Student()
    student.email = request.POST.get('email')
    student.name = request.POST.get('name')
    student.std = request.POST.get('std')
    student.rollno = request.POST.get('rollno')
    student.city = request.POST.get('city')
    student.save()
    # student.email=
    #     email= email,
    #     'name': name,
    #     'std': std,
    #     'rollno': rollno,
    #     'city': city,
    # )

    # f = open("./db/student_list.json", "r")
    # student_list = json.loads(f.read())["stud"]
    # student_list.append(student)
    # f = open("./db/student_list.json", "w")
    # f.write(json.dumps({'stud': student_list}))
    # f.close()
    print(student.__dict__)

    return render(request, 'register/registration_done.html ', student.__dict__)

