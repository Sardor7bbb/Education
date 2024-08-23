from rest_framework import serializers

from users.models import UserModel
from .models import CourseModel


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = ['id', 'group', 'name', 'subject', 'student', 'mentor']


class CourseUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name']


class CourseListSerializer(serializers.ModelSerializer):
    student = CourseUserListSerializer()
    mentor = CourseUserListSerializer()

    class Meta:
        model = CourseModel
        fields = ['group', 'name', 'subject', 'student', 'mentor']
