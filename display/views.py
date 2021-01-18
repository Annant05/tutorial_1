from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import json

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from register.models import Student
from register.serializers import StudentSerializer


def index(request):
    if request.method == "GET":
        # f = open("./db/student_list.json", "r")
        # student_list = json.loads(f.read())["stud"]
        student_list = Student.objects.values()
        return render(request, 'display/table.html ', {"student_list": student_list})


def search(request):
    if request.method == "POST":
        searched_rollno = request.POST.get('search_box')
        student_list = Student.objects.filter(rollno=searched_rollno).values()
        print(student_list)
        if len(student_list) == 0:
            return HttpResponse("Roll number not found!")
        else:
            return render(request, 'display/search_display.html ', {"student_list": student_list})


#        return HttpResponse("Roll number not found!")


def delete_entry(request):
    delete_rollno = request.POST.get('delete_rollno')
    student_list = Student.objects.filter(rollno=delete_rollno).delete()

    return redirect('/display/')
