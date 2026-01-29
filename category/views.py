from drf_spectacular.utils import extend_schema
from utils.base.views_base import BaseUserViewSet
from .models import Category, PriceList, Consultation
from .serializers import CategorySerializer, PriceListSerializer, ConsultationSerializer


@extend_schema(tags=['Category'])
class CategoryViewSet(BaseUserViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@extend_schema(tags=['PriceList'])
class PriceListViewSet(BaseUserViewSet):
    queryset = PriceList.objects.all()
    serializer_class = PriceListSerializer


@extend_schema(tags=['Consultation'])
class ConsultationViewSet(BaseUserViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
