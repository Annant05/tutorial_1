from django.urls import path

from . import views
from .views import ListStudents

urlpatterns = [
    path('', views.index, name='index'),
    path('search_display', views.search),
    path('display', views.delete_entry),
    path('api/', ListStudents.as_view()),
]
