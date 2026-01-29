from drf_spectacular.utils import extend_schema
from doctor.models import Doctor, Stickers
from doctor.serializers import DoctorSerializer, StickersSerializer
from utils.base.views_base import BaseUserViewSet


@extend_schema(tags=['Doctor'])
class DoctorViewSet(BaseUserViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


@extend_schema(tags=['Stickers'])
class StickersViewSet(BaseUserViewSet):
    queryset = Stickers.objects.all()
    serializer_class = StickersSerializer
