from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from user.models import User
from user.serializers.auth_serializers import MeSerializer
from user.serializers.user_serializers import UserCreateSerializer
from utils.base.views_base import PartialPutMixin
from rest_framework.views import APIView
from rest_framework.response import Response


@extend_schema(tags=["User"])
class UserViewSet(PartialPutMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = UserCreateSerializer


@extend_schema(tags=["Profile"])
class MeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MeSerializer

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)
