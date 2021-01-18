from django.urls import path

# from .views import ListStudents
from .views import AllStudents, RegisterStudent

urlpatterns = [
    path('allstudents/', AllStudents.as_view()),
    path('registerstudent/', RegisterStudent.as_view()),
]
