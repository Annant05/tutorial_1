import json

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'register/register.html')


student_list = []


def registered(request):
    email = request.POST.get('email')
    name = request.POST.get('name')
    std = request.POST.get('std')
    rollno = request.POST.get('rollno')
    city = request.POST.get('city')

    student = {
        'email': email,
        'name': name,
        'std': std,
        'rollno': rollno,
        'city': city,
    }

    f = open("./db/student_list.json", "r")
    student_list = json.loads(f.read())["stud"]
    student_list.append(student)
    f = open("./db/student_list.json", "w")
    f.write(json.dumps({'stud': student_list}))
    f.close()

    return render(request, 'register/registration_done.html ', student)
