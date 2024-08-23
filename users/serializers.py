from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import UserModel


class CreateUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'age', 'role', 'phone', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords must match."})
        return data

    def create(self, validated_data):
        user = UserModel(
            phone=validated_data['phone'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            age=validated_data['age'],
            role=validated_data['role'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def to_representation(self, instance):
        data = super(CreateUserSerializer, self).to_representation(instance)
        refresh = RefreshToken.for_user(instance)
        data['access_token'] = str(refresh.access_token)
        return data


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        phone = data.get('phone')
        password = data.get('password')

        try:
            user = UserModel.objects.get(phone=phone)
        except UserModel.DoesNotExist:
            raise serializers.ValidationError({"phone": "Invalid phone number or password."})

        if not user.check_password(password):
            raise serializers.ValidationError({"password": "Invalid phone number or password."})

        # Generate JWT token
        refresh = RefreshToken.for_user(user)
        data['access_token'] = str(refresh.access_token)
        data['refresh_token'] = str(refresh)

        return data
