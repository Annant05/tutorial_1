
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_display',views.search),
    path('display',views.delete_entry)
]