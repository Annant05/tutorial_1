from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from register.models import Student
from register.serializers import StudentSerializer


class AllStudents(APIView):
    @staticmethod
    # @csrf_exempt
    def student_list(request):
        """
        List all code students, or create a new student.
        """
        if request.method == 'GET':
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return serializer.data
            # return JsonResponse(serializer.data, safe=False)
        #
        # elif request.method == 'POST':
        #     data = JSONParser().parse(request)
        #     serializer = StudentSerializer(data=data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return JsonResponse(serializer.data, status=201)
        #     return JsonResponse(serializer.errors, status=400)

    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        """
        Return a list of all students.
        """
        err = False
        message = "List of Students"
        # usernames = [user.username for user in User.objects.all()]
        return Response(
            {
                'error': err,
                'details': message,
                'response': self.student_list(request)
            },
            status=status.HTTP_200_OK
        )


class RegisterStudent(APIView):

    @staticmethod
    def saveStudentToDB(request):
        # print(
        #     JSONParser().parse(request)
        # )
        data = JSONParser().parse(request)
        print(data)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors

    def post(self, request):
        """
        ADD a new student to the database.
        """
        err = False
        message = "New student added"
        return Response(
            {
                'error': err,
                'details': message,
                'response': self.saveStudentToDB(request)
            },
            status=status.HTTP_200_OK
        )
