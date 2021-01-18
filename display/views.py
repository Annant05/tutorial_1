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


class ListStudents(APIView):
    @staticmethod
    @csrf_exempt
    def student_list(request):
        """
        List all code students, or create a new student.
        """
        if request.method == 'GET':
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = StudentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)

    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        # usernames = [user.username for user in User.objects.all()]
        return self.student_list(request)
