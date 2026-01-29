from rest_framework import serializers
from user.models import User
from user.services.user_service import UserService


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'role', 'is_active', 'is_superuser',)


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return UserService.create_user(validated_data)

    def update(self, instance, validated_data):
        return UserService.update_user(instance, validated_data)
