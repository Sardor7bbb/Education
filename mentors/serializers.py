from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from mentors.models import Mentor
from users.models import UserModel


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ['bio', 'speciality']

    def create(self, validated_data):
        user = self.context['request'].user

        if user.role != 'Mentor':
            raise serializers.ValidationError("You are not authorized to create a mentor profile.")

        if Mentor.objects.filter(user=user).exists():
            raise serializers.ValidationError("Mentor profile already exists for this user.")

        return Mentor.objects.create(user=user, **validated_data)


class MentorDetailSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(source='mentor_profile.bio', read_only=True)
    speciality = serializers.CharField(source='mentor_profile.speciality', read_only=True)

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'age', 'phone', 'bio', 'speciality']
