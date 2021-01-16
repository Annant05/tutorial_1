from django.http import HttpResponse
from django.shortcuts import render, redirect
import json

# Create your views here.
from register.models import Student


def index(request):
    if request.method == "GET":
        # f = open("./db/student_list.json", "r")
        # student_list = json.loads(f.read())["stud"]
        student_list = Student.objects.values()
        return render(request, 'display/table.html ', {"student_list": student_list})


def search(request):
    if request.method == "POST":
        searched_rollno = request.POST.get('search_box')
        student_list=Student.objects.filter(rollno=searched_rollno).values()
        print(student_list)
        if len(student_list)==0:
            return HttpResponse("Roll number not found!")
        else:
            return render(request, 'display/search_display.html ', {"student_list": student_list})

#        return HttpResponse("Roll number not found!")


def delete_entry(request):
    delete_rollno = request.POST.get('delete_rollno')
    student_list = Student.objects.filter(rollno=delete_rollno).delete()


    return redirect('/display/')
