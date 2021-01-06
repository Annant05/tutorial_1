from django.http import HttpResponse
from django.shortcuts import render, redirect
import json
# Create your views here.

def index(request):
    if request.method=="GET":
         f = open("./db/student_list.json", "r")
         student_list = json.loads(f.read())["stud"]

         return render(request, 'display/table.html ', {"student_list":student_list})

def search(request):
    if request.method=="POST":
        searched_rollno = request.POST.get('search_box')
        f = open("./db/student_list.json", "r")
        student_list = json.loads(f.read())["stud"]
        for student in student_list:
            if student['rollno']==searched_rollno:
                return render(request, 'display/search_display.html ', {"student_list":[student]})

        return HttpResponse("Roll number not found!")

def delete_entry(request):
    delete_rollno = request.POST.get('delete_rollno')
    print("line 26 ", delete_rollno)
    f = open("./db/student_list.json", "r")
    student_list = json.loads(f.read())["stud"]
    for student in student_list:
        if student['rollno'] == delete_rollno:
            print(student_list)
            student_list.remove(student)
            print(student_list)
            f = open("./db/student_list.json", "w")
            f.write(json.dumps({'stud': student_list}))
            f.close()


    return redirect('/display/')
