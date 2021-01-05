from django.shortcuts import render
import json
# Create your views here.

def index(request):
    f = open("./db/student_list.json", "r")
    student_list = json.loads(f.read())["stud"]
    print({"student_list":student_list})

    return render(request, 'display/table.html ', {"student_list":student_list})