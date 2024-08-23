from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from courses.models import CourseModel
from parents.models import Parent
from users.models import UserModel


class ParentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    children = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.filter(role='User'))

    class Meta:
        model = Parent
        fields = ['user', 'children']

    def create(self, validated_data):
        user = self.context['request'].user
        children = validated_data.pop('children')
        parent = Parent.objects.create(user=user, children=children)
        return parent


class CourseSerializer(serializers.ModelSerializer):
    mentor = serializers.StringRelatedField()

    class Meta:
        model = CourseModel
        fields = ['group', 'name', 'subject', 'mentor']


class ChildrenListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    children = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.filter(role='User'), many=True)
    child_courses = serializers.SerializerMethodField()

    class Meta:
        model = Parent
        fields = ['user', 'children', 'child_courses']

    def get_child_courses(self, obj):
        child_ids = obj.children.values_list('id', flat=True)
        child_courses = CourseModel.objects.filter(student__in=child_ids)
        return CourseSerializer(child_courses, many=True).data


