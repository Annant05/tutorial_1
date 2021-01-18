from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from register.models import Student


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['email', 'rollno', 'name', 'std', 'city']

#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']
