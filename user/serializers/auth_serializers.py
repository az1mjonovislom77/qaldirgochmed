from rest_framework import serializers
from user.models import User
from user.services.auth_service import AuthService


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = AuthService.authenticate_user(username=attrs.get('username'), password=attrs.get('password'))
        attrs['user'] = user
        return attrs


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def save(self, **kwargs):
        AuthService.logout_user(self.validated_data['refresh'])


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "username", "role",)
        extra_kwargs = {"id": {"read_only": True}, }

    def validate_username(self, value):
        return value

    def update(self, instance, validated_data):
        instance.name = (validated_data.get("name", instance.name))
        instance.username = (validated_data.get("username", instance.username))
        instance.role = validated_data.get("role", instance.role)
        instance.save()
        return instance
